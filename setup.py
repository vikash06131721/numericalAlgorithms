from distutils.core import setup
setup(
  name = 'numericalPython',       
  packages = ['numericalPython'],   # Chose the same as "name"
  version = '0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The package can be used for AUTOML',   
  author = 'Vikash Kumar Prasad',                   # Type in your name
  author_email = 'ubuntukr7@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vikash06131721/autoMltext',   # Provide either the link to your github or to your website
#   download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['text', 'automl'],   # Keywords that define your package best

  # install_requires =[
  #   "scikit-learn==0.24.0",
  #   "joblib==1.0.1",
  #   "numpy==1.21.4",
  #   "nltk==3.5",
  #   "stop_words"
  # ],

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8'     #Specify which pyhton versions that you want to support
  ],
)