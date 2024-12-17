import pandas as pd
import xml.etree.ElementTree as ET
from typing import Union, List, Dict
import pathlib

def xml_to_dataframe(xml_source: Union[str, pathlib.Path], 
                     root_element: str = None,
                     record_tag: str = None) -> pd.DataFrame:
    """
    Convert XML data to a pandas DataFrame.
    
    Parameters:
    -----------
    xml_source : str or Path
        Path to XML file or XML string content
    root_element : str, optional
        Specific element to use as root for parsing
    record_tag : str, optional
        Specific tag to use as record delimiter
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing the parsed XML data
    """
    try:
        # Check if input is a file path or XML string
        if isinstance(xml_source, (str, pathlib.Path)) and pathlib.Path(xml_source).exists():
            tree = ET.parse(xml_source)
            root = tree.getroot()
        else:
            root = ET.fromstring(xml_source)
            
        # Navigate to specified root element if provided
        if root_element:
            root = root.find(root_element)
            if root is None:
                raise ValueError(f"Root element '{root_element}' not found")
        
        # Find all records based on record_tag or use immediate children
        if record_tag:
            records = root.findall(f'.//{record_tag}')
        else:
            records = list(root)
            
        if not records:
            raise ValueError("No records found in XML")
            
        def element_to_dict(element: ET.Element) -> Dict:
            """Convert an XML element and its children to a dictionary"""
            result = {}
            
            # Add element's attributes
            result.update(element.attrib)
            
            # Add element's text if it exists
            if element.text and element.text.strip():
                result['text'] = element.text.strip()
                
            # Process child elements
            for child in element:
                child_data = element_to_dict(child)
                
                # Handle nested elements
                if child.tag in result:
                    # Convert to list if multiple elements with same tag
                    if isinstance(result[child.tag], list):
                        result[child.tag].append(child_data)
                    else:
                        result[child.tag] = [result[child.tag], child_data]
                else:
                    result[child.tag] = child_data
                    
            return result
        
        # Convert all records to list of dictionaries
        data = [element_to_dict(record) for record in records]
        
        # Create DataFrame
        df = pd.json_normalize(data)
        
        return df
        
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML format: {str(e)}")
    except Exception as e:
        raise Exception(f"Error processing XML: {str(e)}")