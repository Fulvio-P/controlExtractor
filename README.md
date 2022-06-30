# controlExtractor
Control extractor is tool for automatic control elicitation for the Italian Cybersecurity Framework

## Dependencies
Control extractor needs the following packages to works:
- openpyxl: https://pypi.org/project/openpyxl/
- natsort: https://pypi.org/project/natsort/

## Usage

### Basic usage:
Edit "config.JSON" to select elicitation rules, then run:

`
python controlExtractor.py <security_templates_path> <output_xlsx_path>
`

<security_templates_path> must respect the structre of the "Security Templates" example, but it is possible to remove any unwanted function, category or subcategory by deleting the corresponding files.

<output_xlsx_path> does not have to be an existing xlsx file. If the file exists it will be overwritten, otherwise it will be created.

### Quick guide
To use controlExtractor:
1. Select from the Framework categories and subcategories for control elicitation;
2. Edit "config.JSON" to select the elicitation rules to apply;
3. Delete from the directories inside "Security Templates" all the files correspondind to all the unselected categories and subcategories;
4. Run the tool with the command below;

`
python controlExtractor.py Security\ Templates output.xlsx
`

### Other options
To generate controls without pre-appending an ID to each of them:

`
python controlExtractor.py <security_templates_path> <output_xlsx_path> -n
`
## Elicitation Rules
- nodeExist -> creates a control requiring the existance of each Process and Data Store;
- nodeC -> creates a control for each Node with confidentiality requirements;
- nodeI -> creates a control for each Node with integrity requirements;
- nodeA -> creates a control for each Node with availability requirements;
- nodeCIA -> applies nodeC, nodeI and nodeA but creates a single control per node;
- flowExist -> creates a control requiring the existance of each Data Flow;
- flowC -> creates a control for each Data Flow with confidentiality requirements;
- flowI -> creates a control for each Data Flow with integrity requirements;
- flowA -> creates a control for each Data Flow with availability requirements;
- flowP -> creates a control for each Personal Data Flow;
- flowCIAP -> applies flowC, flowI, flowA and flowP but creates a single control per Data Flow;
- areaExist -> creates a control requiring the existance of each Area;
- areaTrust -> creates a control for each Trust Area;
- areaFlowsEnter -> creates a control for each Data Flow entering inside an Area;
- areaFlowsExit -> creates a control for each Data Flow exiting from an Area;

Do not run nodeCIA or flowCIAP when any of the single rules inlcuded in them is active to avoid redundancy.
