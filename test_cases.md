# Component Test Cases

## Selection Components

### select_single_cards Test Cases

1. **Basic Loan Type Selection**
   ```json
   {
     "screen_template_id": "fa37d276-abc0-4fe3-b840-909e1c0b26d2",
     "name": "first_loan_type",
     "state": "draft",
     "title": "What kind of loan will you have?",
     "label": "Loan Type",
     "description": "Will it be Conventional, FHA, VA, or another type?",
     "stage": "basics",
     "section": "funds_and_financing",
     "scope": {
       "funds_type_loan": true
     },
     "tips": "Most individuals use Conventional loans, but FHA and VA loans are more specialized and require additional diligence.",
     "tip_links": {
       "Loan Types Explained": {
         "label": "Loan Types Explained",
         "url": "https://www.homebuyme.com/insights/loan-types-explained"
       }
     },
     "small_print": "FHA and VA loans will require additional lender requirements.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "LOAN-TYPE-2024-001",
       "notes": "Critical for determining loan-specific screens and requirements"
     },
     "components": {
       "first_loan_type": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "select_single_cards",
         "name": "first_loan_type",
         "is_array": true,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "array",
           "required": true
         },
         "formatting": null,
         "tooltip": "Select your loan type",
         "fields": [],
         "logic": [],
         "children": [
           {
             "id": "159202dc-6c44-443e-829a-c2246b44af13",
             "component_type": "select_card",
             "name": "first_loan_type_conventional",
             "is_array": false,
             "is_private": false,
             "is_editable": true,
             "is_required": false,
             "is_visible": true,
             "default_value": true,
             "value": null,
             "suggested": null,
             "validation": null,
             "formatting": null,
             "tooltip": "Conventional loan",
             "fields": [
               {
                 "id": "f050d526-6b8d-488f-92bc-81dac2a06c6a",
                 "name": "label",
                 "label": null,
                 "value": "Conventional"
               },
               {
                 "id": "4f2b3655-ffcd-4f87-a045-4f216c7b0640",
                 "name": "description",
                 "label": null,
                 "value": "Traditional mortgage loan"
               },
               {
                 "id": "d5c97511-ba9f-458c-8141-1f8cafe720ba",
                 "name": "image",
                 "label": null,
                 "value": "15_house_dollarsign.png"
               }
             ],
             "logic": [],
             "children": []
           }
         ]
       }
     }
   }
   ```

2. **Funds Type Selection**
   ```json
   {
     "screen_template_id": "8ec42117-858b-43b5-994c-3210c18e0bda",
     "name": "funds_type",
     "state": "draft",
     "title": "How will you pay for the property?",
     "label": "Payment Type",
     "description": "Will you pay in cash or use a loan?",
     "stage": "basics",
     "section": "funds_and_financing",
     "scope": {},
     "tips": "All cash offers are often more attractive to sellers as they eliminate financing contingencies.",
     "tip_links": {},
     "small_print": "Your selection will determine the required documentation and contingencies.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "FUNDS-TYPE-2024-001",
       "notes": "Determines if loan-specific screens are needed"
     },
     "components": {
       "funds_type": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "select_single_cards",
         "name": "funds_type",
         "is_array": true,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "array",
           "required": true
         },
         "formatting": null,
         "tooltip": "Select your payment type",
         "fields": [],
         "logic": [],
         "children": [
           {
             "id": "159202dc-6c44-443e-829a-c2246b44af13",
             "component_type": "select_card",
             "name": "funds_type_cash",
             "is_array": false,
             "is_private": false,
             "is_editable": true,
             "is_required": false,
             "is_visible": true,
             "default_value": false,
             "value": null,
             "suggested": null,
             "validation": null,
             "formatting": null,
             "tooltip": "All cash payment",
             "fields": [
               {
                 "id": "f050d526-6b8d-488f-92bc-81dac2a06c6a",
                 "name": "label",
                 "label": null,
                 "value": "All Cash"
               },
               {
                 "id": "4f2b3655-ffcd-4f87-a045-4f216c7b0640",
                 "name": "description",
                 "label": null,
                 "value": "You will pay in all cash"
               },
               {
                 "id": "d5c97511-ba9f-458c-8141-1f8cafe720ba",
                 "name": "image",
                 "label": null,
                 "value": "cash_icon.png"
               }
             ],
             "logic": [
               {
                 "rule": {
                   "id": "e266f509-0fee-4714-9170-561a12095862",
                   "condition": {
                     "id": "a2d17973-2176-4796-b2f0-9497d4041831",
                     "path": "this.value",
                     "operator": "equals",
                     "value": true
                   },
                   "action": {
                     "id": "b43583ce-008d-476d-a816-a4c15d98805e",
                     "path": "globals",
                     "operation": "set",
                     "value": {
                       "name": "funds_type_cash",
                       "value": true
                     }
                   }
                 }
               }
             ],
             "children": []
           }
         ]
       }
     }
   }
   ```

### select_single_dropdown Test Cases

1. **Basic Dropdown Selection**
   ```json
   {
     "screen_template_id": "b2ce4f6a-0656-4da3-9756-04698d7e2e51",
     "name": "occupancy_type",
     "state": "draft",
     "title": "How will you use this property?",
     "label": "Occupancy Type",
     "description": "Select how you plan to use this property",
     "stage": "basics",
     "section": "property_details",
     "scope": {},
     "tips": "Your occupancy type affects loan requirements and tax implications.",
     "tip_links": {},
     "small_print": "Different occupancy types may have different requirements and restrictions.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "OCCUPANCY-2024-001",
       "notes": "Affects loan type and requirements"
     },
     "components": {
       "occupancy_type": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "select_single_dropdown",
         "name": "occupancy_type",
         "is_array": true,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "array",
           "required": true
         },
         "formatting": null,
         "tooltip": "Select occupancy type",
         "fields": [],
         "logic": [],
         "children": [
           {
             "id": "159202dc-6c44-443e-829a-c2246b44af13",
             "component_type": "select_option",
             "name": "occupancy_type_primary",
             "is_array": false,
             "is_private": false,
             "is_editable": true,
             "is_required": false,
             "is_visible": true,
             "default_value": true,
             "value": null,
             "suggested": null,
             "validation": null,
             "formatting": null,
             "tooltip": "Primary residence",
             "fields": [
               {
                 "id": "f050d526-6b8d-488f-92bc-81dac2a06c6a",
                 "name": "label",
                 "label": null,
                 "value": "Primary Residence"
               },
               {
                 "id": "4f2b3655-ffcd-4f87-a045-4f216c7b0640",
                 "name": "description",
                 "label": null,
                 "value": "This will be your main home"
               }
             ],
             "logic": [],
             "children": []
           }
         ]
       }
     }
   }
   ```

## Text Input Components

### input_text_line Test Cases

1. **Basic Text Input**
   ```json
   {
     "screen_template_id": "a129a8e1-0793-4b5c-bb1a-419c2836be50",
     "name": "customer_nickname",
     "state": "draft",
     "title": "What's your first name?",
     "label": "First Name",
     "description": "Enter your first name as it appears on your ID",
     "stage": "basics",
     "section": "personal_info",
     "scope": {},
     "tips": "Use your legal first name as it appears on your government-issued ID.",
     "tip_links": {},
     "small_print": "This information will be used for official documents.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "NAME-2024-001",
       "notes": "Used for personalization and legal documents"
     },
     "components": {
       "customer_nickname": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "input_text_line",
         "name": "customer_nickname",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "string",
           "required": true,
           "min_length": 1,
           "max_length": 50
         },
         "formatting": null,
         "tooltip": "Enter your first name",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

2. **Text Input with Specific Validation**
   ```json
   {
     "input": {
       "component_type": "input_text_line",
       "name": "phone_number",
       "label": "What's your phone number?",
       "placeholder": "(555) 555-5555",
       "validation": {
         "pattern": "^\\d{10}$",
         "error_message": "Please enter a valid 10-digit phone number"
       }
     },
     "expected_output": {
       "id": "uuid-format",
       "component_type": "input_text_line",
       "name": "phone_number",
       "is_array": false,
       "is_required": true,
       "is_visible": true,
       "validation": {
         "value_type": "string",
         "required": true,
         "pattern": "^\\d{10}$",
         "error_message": "Please enter a valid 10-digit phone number"
       }
     }
   }
   ```

### input_text_area Test Cases

1. **Basic Multi-line Input**
   ```json
   {
     "screen_template_id": "9e8d5186-229a-49a0-a8a6-28eed955d35f",
     "name": "additional_fees",
     "state": "draft",
     "title": "Additional Fees",
     "label": "Additional Fees",
     "description": "Enter any additional fees or charges",
     "stage": "basics",
     "section": "fees",
     "scope": {},
     "tips": "Include any fees that are not part of the standard closing costs.",
     "tip_links": {},
     "small_print": "All fees must be documented and agreed upon by both parties.",
     "is_required": false,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "FEES-2024-001",
       "notes": "Additional fees documentation"
     },
     "components": {
       "additional_fees": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "input_text_area",
         "name": "additional_fees",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "string",
           "required": false,
           "min_length": 0,
           "max_length": 1000
         },
         "formatting": null,
         "tooltip": "Enter additional fees",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

### input_email Test Cases

1. **Basic Email Input**
   ```json
   {
     "screen_template_id": "e04ae9d3-5c71-42f7-b7c1-fee995df66d9",
     "name": "seller1_email_fsbo",
     "state": "draft",
     "title": "What's your email address?",
     "label": "Email Address",
     "description": "Enter your email address for communication",
     "stage": "basics",
     "section": "contact_info",
     "scope": {},
     "tips": "We'll use this email to send you important documents and updates.",
     "tip_links": {},
     "small_print": "Your email will be used for official communication.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "EMAIL-2024-001",
       "notes": "Primary communication channel"
     },
     "components": {
       "seller1_email_fsbo": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "input_email",
         "name": "seller1_email_fsbo",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "string",
           "required": true,
           "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
           "error_message": "Please enter a valid email address"
         },
         "formatting": null,
         "tooltip": "Enter your email address",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

## Numeric Input Components

### input_number Test Cases

1. **Basic Number Input**
   ```json
   {
     "screen_template_id": "e7358a01-f226-4932-88d4-5cec81cea202",
     "name": "escalation_clause",
     "state": "draft",
     "title": "Escalation Clause",
     "label": "Escalation Amount",
     "description": "Enter the escalation amount",
     "stage": "basics",
     "section": "offer_terms",
     "scope": {},
     "tips": "The escalation amount is the maximum amount you're willing to increase your offer.",
     "tip_links": {},
     "small_print": "This amount will be used to automatically increase your offer if there are competing offers.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "ESCALATION-2024-001",
       "notes": "Maximum escalation amount"
     },
     "components": {
       "escalation_clause": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "input_number",
         "name": "escalation_clause",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "number",
           "required": true,
           "min": 0,
           "max": 1000000,
           "step": 1000
         },
         "formatting": null,
         "tooltip": "Enter escalation amount",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

### input_currency Test Cases

1. **Basic Currency Input**
   ```json
   {
     "screen_template_id": "e96068d1-5b60-4dc8-8221-1614583dde14",
     "name": "property_listing_price",
     "state": "draft",
     "title": "Property Listing Price",
     "label": "Listing Price",
     "description": "Enter the property listing price",
     "stage": "basics",
     "section": "property_details",
     "scope": {},
     "tips": "Enter the price as listed by the seller.",
     "tip_links": {},
     "small_print": "This price will be used as the base for your offer.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "PRICE-2024-001",
       "notes": "Base price for offer calculations"
     },
     "components": {
       "property_listing_price": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "input_currency",
         "name": "property_listing_price",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "number",
           "required": true,
           "min": 0,
           "max": 1000000000,
           "step": 1000,
           "currency": "USD"
         },
         "formatting": null,
         "tooltip": "Enter listing price",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

### input_percentage Test Cases

1. **Basic Percentage Input**
   ```json
   {
     "screen_template_id": "ea785610-1857-48c8-a278-f4887d3956bb",
     "name": "first_loan_points",
     "state": "draft",
     "title": "Loan Points",
     "label": "Points",
     "description": "Enter the number of points for your loan",
     "stage": "basics",
     "section": "loan_details",
     "scope": {},
     "tips": "Points are fees paid to the lender to reduce the interest rate.",
     "tip_links": {},
     "small_print": "Each point typically costs 1% of the loan amount.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "POINTS-2024-001",
       "notes": "Loan points calculation"
     },
     "components": {
       "first_loan_points": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "input_percentage",
         "name": "first_loan_points",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "number",
           "required": true,
           "min": 0,
           "max": 5,
           "step": 0.25,
           "is_percentage": true
         },
         "formatting": null,
         "tooltip": "Enter loan points",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

## Date and File Components

### pick_date_time Test Cases

1. **Basic Date Input**
   ```json
   {
     "screen_template_id": "e720e4c4-c24c-42be-88f6-c26ff0246a15",
     "name": "coe_number_of_days",
     "state": "draft",
     "title": "Close of Escrow Date",
     "label": "COE Date",
     "description": "Select the close of escrow date",
     "stage": "basics",
     "section": "timeline",
     "scope": {},
     "tips": "This is the date when the property ownership will transfer to you.",
     "tip_links": {},
     "small_print": "The COE date must be agreed upon by all parties.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "COE-2024-001",
       "notes": "Critical timeline milestone"
     },
     "components": {
       "coe_number_of_days": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "pick_date_time",
         "name": "coe_number_of_days",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "string",
           "required": true,
           "format": "YYYY-MM-DD",
           "min_date": "today",
           "max_date": "2025-12-31"
         },
         "formatting": null,
         "tooltip": "Select COE date",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

### pick_file Test Cases

1. **Basic File Upload**
   ```json
   {
     "screen_template_id": "e72b1e8f-95ad-4779-b70f-578fa9c631d4",
     "name": "preapproval_letter_uploader",
     "state": "draft",
     "title": "Pre-approval Letter",
     "label": "Upload Letter",
     "description": "Upload your pre-approval letter",
     "stage": "basics",
     "section": "loan_documents",
     "scope": {},
     "tips": "Your pre-approval letter should be from your lender and include the loan amount.",
     "tip_links": {},
     "small_print": "The letter must be current and from an approved lender.",
     "is_required": true,
     "is_private": false,
     "is_editable": true,
     "internal": {
       "references": "PREAPPROVAL-2024-001",
       "notes": "Required loan documentation"
     },
     "components": {
       "preapproval_letter_uploader": {
         "id": "79565085-434c-4fa8-8b6e-9705a8b934ce",
         "component_type": "pick_file",
         "name": "preapproval_letter_uploader",
         "is_array": false,
         "is_private": false,
         "is_editable": true,
         "is_required": false,
         "is_visible": true,
         "default_value": null,
         "value": null,
         "suggested": null,
         "validation": {
           "value_type": "object",
           "required": true,
           "max_size": 5242880,
           "allowed_types": ["application/pdf", "image/jpeg", "image/png"]
         },
         "formatting": null,
         "tooltip": "Upload pre-approval letter",
         "fields": [],
         "logic": [],
         "children": []
       }
     }
   }
   ```

## Test Case Categories

### 1. Basic Functionality
- Screen metadata validation
- Component structure validation
- Required fields presence
- Default values
- Visibility conditions

### 2. Validation
- Required field validation
- Value type validation
- Pattern matching
- Range validation
- Logic rules validation

### 3. Edge Cases
- Empty values
- Maximum values
- Special characters
- Long text
- File size limits

### 4. Integration
- Parent-child relationships
- Global variable updates
- Conditional logic
- State management
- Screen navigation

### 5. Error Handling
- Invalid input handling
- Missing required fields
- Format validation errors
- File type validation
- Network errors

// ... More test cases to be added for other components ... 