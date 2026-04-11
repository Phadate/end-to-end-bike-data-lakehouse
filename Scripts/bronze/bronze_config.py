BASE_PATH = "/Volumes/bike_lakehouse/bronze/bronze_raw_sources"

INGESTION_DATA = [
    # CRM system
    {
        'table_name': "cust_info_bronze",
        'path': f"{BASE_PATH}/source_crm/cust_info.csv",
        'source' : "crm", 
    },
    {
        'table_name': "prd_info_bronze",
        'path': f"{BASE_PATH}/source_crm/prd_info.csv",
        'source' : "crm", 
    },
    {
        'table_name': "sales_details_bronze",
        'path': f"{BASE_PATH}/source_crm/sales_details.csv",
        'source': "crm", 
    },
    # ERP system
    {
        'table_name': "CUST_AZ12_bronze",
        'path': f"{BASE_PATH}/source_erp/CUST_AZ12.csv",
        'source' : "erp", 
    },
    {
        'table_name': "LOC_A101_bronze",
        'path': f"{BASE_PATH}/source_erp/LOC_A101.csv",
        'source': "erp", 
    },
    {
        'table_name': "PX_CAT_G1V2_bronze",
        'path': f"{BASE_PATH}/source_erp/PX_CAT_G1V2.csv",
        'source': "erp", 
    }
]