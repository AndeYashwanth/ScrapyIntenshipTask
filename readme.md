1) create project scrape_test<br>
2) paste pipelins.py, settings.py, exporters.py from the repo where settings.py file is located.<br>
3) paste main.py, first.py in spiders folder.<br>
4) Edit the FILES_STORE in settings.py with path where you want the files to be downloaded.<br><br>

->  first.py file extracts pdf's from 1st link given in assignment.<br>
->  main.py file extracts pdf's from 2nd, 3rd, 4th link given in assignment.(5th link is not working)<br>
->  pipelines.py file contains custom pipeline to download files with custom filename instead of sha hash.<br>
->  exporters.py file enables us to convert unicode characters when storing the output using -o.<br>
->  settings.py was edited to use custom pipeline, exporter and useragent.<br><br>

<b>To run</b><br>
scrapy crawl spider -o spider.json<br>
scrapy crawl first -o first.json<br><br>

spider.json and first.json contains list of dictionaries.<br>
Each dictionary is associated with each pdf link. It contains keys title(a tag content), filename(name with which file is stored, obtained from last part of url), date(from second level deep), file_urls(pipeline uses to download files), files(dictionary containing keys as url, path, checksum which is created by scrapy automatically)
<br><br>
Note: import urllib.parse was only used to decode the url when getting the filename from url.
