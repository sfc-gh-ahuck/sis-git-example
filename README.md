# Git Integration Demos

## Self contained Demo Script
```sql
-- Context
CREATE DATABASE IF NOT EXISTS DEMO_GIT;
CREATE WAREHOUSE IF NOT EXISTS DEMO_GIT_WH 
    WAREHOUSE_SIZE=XSMALL 
    INITIALLY_SUSPENDED=TRUE;

USE SCHEMA DEMO_GIT.PUBLIC;
USE WAREHOUSE DEMO_GIT_WH;

-- create github api integration
create or replace api integration github_api 
  api_provider = git_https_api
  api_allowed_prefixes = ('https://github.com/')
  allowed_authentication_secrets = all
  enabled = true;

-- show existing integrations
show integrations;

-- create credentials (optional for public repo RO operations)
create or replace secret gh_blank_secret
    type = password
    username = ''
    password = '';

-- create git repository
create git repository if not exists github_sis_example
    origin = 'https://github.com/sfc-gh-ahuck/sis-git-example'
    git_credentials = gh_blank_secret
    api_integration = github_api;
    
-- display repository data
show git repositories like 'github_sis_example';

-- display backing stage storage supporting the local copy of repo
show stages;

-- list branches
show git branches in git repository github_sis_example;

-- list tags
show git tags in git repository github_sis_example;

-- list files
ls @github_sis_example/branches/main;

-- list file details
ls @github_sis_example/branches/main/hello.sql;

-- copy files from SnowGit repo to stage
CREATE OR REPLACE STAGE stage;
copy files into @stage from @github_sis_example/branches/main/;

-- fetch git repository
alter git repository github_sis_example fetch;

-- create snowpark procedure
create or replace procedure hello()
                            returns string
                            language python
                            runtime_version='3.10'
                            packages=('snowflake-snowpark-python')
                            imports=('@github_sis_example/branches/main/sproc-example.py')
                            handler='sproc-example.main';
call hello();

-- create streamlit application
create or replace streamlit streamlit_snowpark_app
root_location = @DEMO_GIT.PUBLIC.github_sis_example/branches/main
main_file = '/sis-example.py'
query_warehouse = 'DEMO_GIT_WH';

-- execute immediate from
-- Say hello
execute immediate from @github_sis_example/branches/main/hello.sql;

-- automate creation of objects
execute immediate from @github_sis_example/branches/main/deploy_hello.sql;
call hello2();

--------------
-- clean up --
--------------
DROP WAREHOUSE IF EXISTS DEMO_GIT_WH;
DROP DATABASE IF EXISTS DEMO_GIT;
```
