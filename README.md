# Locomotion scrapper
## Getting started
### Clone
```
git clone git@github.com:fabienheureux/locomotion-scrapper.git
```
### Installation 
It is strongly advised that you make use of pipenv, if so, inside `scrapper` directory, let's run :
```
pipenv shell
```
then 
```
pipenv install
```
## Running
You can run the command below to trigger scraping of urls specified in spiders files 
```
make crawl
```
## Output
Files will be created under output directory as .csv files.
