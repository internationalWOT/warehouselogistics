# from setuptools import setup, find_packages

# setup(
#     name='logistics_api',
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=[
#         'flask',
#     ],
# )

"""
This script runs the Server application using a development server.
"""
# from dotenv import load_dotenv
import os
from logistics_api import create_app

if __name__ == '__main__':
    app = create_app(os.getenv('config_by_name') or 'dev')
    app.run()
