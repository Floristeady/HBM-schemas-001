import unittest
import pandas as pd
import json
import os
from excel_to_json_converter import ExcelToJsonConverter

class TestExcelToJsonConverter(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        # Create test directory
        os.makedirs('test_data', exist_ok=True)
        os.makedirs('test_output', exist_ok=True)
        
        # Create test data
        self.test_data = pd.DataFrame({
            'Screen_ID': ['test_screen_1', 'test_screen_1'],
            'Screen Name': ['Test Screen', 'Test Screen'],
            'Stage': ['active', 'active'],
            'Title': ['Test Title', 'Test Title'],
            'Label': ['Test Label', 'Test Label'],
            'Description': ['Test Description', 'Test Description'],
            'Component type': ['select_single_cards', 'input_text_line'],
            'Data Format': ['{"required": true}', '{"required": true}'],
            'Tips': ['Test Tips', 'Test Tips'],
            'References': ['TEST_REF', 'TEST_REF'],
            'Small Print': ['Test Small Print', 'Test Small Print'],
            'Options': ['["Yes", "No"]', ''],
            'Default Value': ['Yes', ''],
            'Hard Min / Soft Min': ['0', ''],
            'Soft Max / Hard Max': ['100', '']
        })
        
        # Save as Excel
        self.excel_file = 'test_data/test_screens.xlsx'
        self.test_data.to_excel(self.excel_file, index=False)
        
        # Save as CSV
        self.csv_file = 'test_data/test_screens.csv'
        self.test_data.to_csv(self.csv_file, index=False)
        
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.excel_file):
            os.remove(self.excel_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists('test_output'):
            for file in os.listdir('test_output'):
                os.remove(os.path.join('test_output', file))
            os.rmdir('test_output')
        if os.path.exists('test_data'):
            os.rmdir('test_data')
            
    def test_converter_initialization(self):
        """Test converter initialization"""
        converter = ExcelToJsonConverter(self.excel_file, 'test_output', skiprows_real_csv=False)
        self.assertEqual(converter.input_file, self.excel_file)
        self.assertEqual(converter.output_dir, 'test_output')
        
    def test_excel_reading(self):
        """Test Excel file reading"""
        converter = ExcelToJsonConverter(self.excel_file, 'test_output', skiprows_real_csv=False)
        converter.read_file()
        self.assertIsNotNone(converter.df)
        self.assertEqual(len(converter.df), 2)
        
    def test_csv_reading(self):
        """Test CSV file reading"""
        converter = ExcelToJsonConverter(self.csv_file, 'test_output', skiprows_real_csv=False)
        converter.read_file()
        self.assertIsNotNone(converter.df)
        self.assertEqual(len(converter.df), 2)
        
    def test_data_validation(self):
        """Test data validation"""
        converter = ExcelToJsonConverter(self.excel_file, 'test_output', skiprows_real_csv=False)
        converter.read_file()
        self.assertTrue(converter.validate_data())
        
    def test_json_conversion(self):
        """Test JSON conversion and file creation"""
        converter = ExcelToJsonConverter(self.excel_file, 'test_output', skiprows_real_csv=False)
        converter.convert()
        
        # Check if output file exists
        output_file = os.path.join('test_output', 'test_screen_1.json')
        self.assertTrue(os.path.exists(output_file))
        
        # Check JSON structure
        with open(output_file, 'r') as f:
            json_data = json.load(f)
            
        self.assertEqual(json_data['screen_template_id'], 'test_screen_1')
        self.assertEqual(json_data['name'], 'Test Screen')
        self.assertEqual(len(json_data['components']), 2)
        
        # Check component fields
        component = json_data['components'][0]
        self.assertEqual(component['component']['type'], 'select_single_cards')
        self.assertEqual(component['tips'], 'Test Tips')
        self.assertEqual(component['internal_reference'], 'TEST_REF')
        self.assertEqual(component['small_print'], 'Test Small Print')
        self.assertEqual(component['options'], '["Yes", "No"]')
        self.assertEqual(component['default_value'], 'Yes')
        self.assertEqual(component['min_value'], '0')
        self.assertEqual(component['max_value'], '100')
        
if __name__ == '__main__':
    unittest.main() 