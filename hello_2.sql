create or replace procedure hello()
                            returns string
                            language python
                            runtime_version='3.10'
                            packages=('snowflake-snowpark-python')
                            imports=('@github_sis_example/branches/main/sproc-example.py')
                            handler='sproc-example.main';
