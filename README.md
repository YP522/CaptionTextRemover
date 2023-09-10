# CaptionTextRemover [EXPERIMENTAL]

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=YP522_CaptionTextRemover&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=YP522_CaptionTextRemover) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=YP522_CaptionTextRemover&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=YP522_CaptionTextRemover) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=YP522_CaptionTextRemover&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=YP522_CaptionTextRemover) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=YP522_CaptionTextRemover&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=YP522_CaptionTextRemover) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=YP522_CaptionTextRemover&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=YP522_CaptionTextRemover)

 Remove a Caption-Text from a picture

> ## This project is no longer actively maintained
>
> Originally, it was an experimental test aimed at removing a "caption-text" filter from a snap, while avoiding methods where the values would be too far apart, like the risk of "content-fill aware" applied to the entire banner, for example, where the deviations from the original colors are significant. However, this project is currently not actively maintained. Nevertheless, it may receive updates in the future.


<p align="center">
  <img src="https://ypetit.web-edu.fr/captiontextremover/CaptionTextRemover_banner.png" title="CaptionTextRemover">
</p>

## Features

- Recovery of the original pixel by "subtracting" a colour with alpha from an rgb colour (low differential margin)
- Doc File with text

## How to run ?
First, extract the caption text with a raster graphics editor.
Then, run this selection with `py .\ctr.py run-extra 'img.png' 0 0 0 150 221 120 255 32 0 150 2 11` (for example)

Download Source Code Project, Install dependencies and run this command :
`py .\ctr.py run-extra image_path red green blue alpha value_correction threshold1 minval1 inpaintmethod1 threshold2 minval2 size inpaintmethod2`

or download executable here :
https://ypetit.web-edu.fr/captiontextremover/download/0.0.0/CaptionTextRemover.exe

## Learn how to use ?
Read the tutorial step by step here : https://ypetit.web-edu.fr/captiontextremover/get-started/
Running may take a few minutes to a few hours

## Commands
Open the list of commands
`py .\ctr.py help`

Get the version of ctr project
`py .\ctr.py version`

Learn more about ctr project
`py .\ctr.py about`
    
Learn about author(s)
`py .\ctr.py credits`

Run ctr with 1 image file
`py .\ctr.py run image_path red green blue alpha value_correction`

Run ctr with 1 image file
`py .\ctr.py run-extra image_path red green blue alpha value_correction threshold1 minval1 inpaintmethod1 threshold2 minval2 size inpaintmethod2`

## Disclaimer
### Code
This project is opensource in order to share a concept.
The code is not necessarily clean.

If you are interested in improving CaptionTextRemover, don't hesitate to join the project ! 

The next missions are :

1. Code maintenance (python best practices)

2. Reduce package usage

3. Reduce processing time