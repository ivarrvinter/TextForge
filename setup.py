from setuptools import setup, find_packages

setup(
    name='TextForge',
    version='0.1.0',
    packages=find_packages(),
    description="TextForge is a powerful library designed to facilitate text cleaning and preprocessing tasks.",
    long_description="TextForge is a powerful library designed to facilitate text cleaning and preprocessing tasks. Currently, it specializes in cleaning and sanitizing tweets, ensuring that they are ready for further analysis or natural language processing (NLP) tasks. We are actively working on expanding its capabilities and adding more features to make it a comprehensive text processing toolkit.",
    author="Ivarr Vinter",
    author_email="ivarrvinter@gmail.com",
    url="https://github.com/ivarrvinter/TextForge",
    license='MIT',
    keywords=['nlp', 'text preprocessing', 'text cleaning', 'text mining'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: IDLE',
        'Framework :: Jupyter',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing',
    ],
    requires=[
        're',
    ],
)