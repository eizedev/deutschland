# jobsuche
Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/bundesAPI/deutschland.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bundesAPI/deutschland.git`)

Then import the package:
```python
from deutschland import jobsuche
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
from deutschland import jobsuche
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
from deutschland import jobsuche
from pprint import pprint
from deutschland.jobsuche.api import default_api
from deutschland.jobsuche.model.job_application_details import JobApplicationDetails
from deutschland.jobsuche.model.job_details import JobDetails
from deutschland.jobsuche.model.job_search_response import JobSearchResponse
# Defining the host is optional and defaults to https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    hash_id = "VK2qoXBe0s-UAdH_qxLDRrZrY5iY8a1PJt3MjJCXsdo=" # str | 

    try:
        # Unternehmen Logo
        api_response = api_instance.ed_v1_arbeitgeberlogo_hash_id_get(hash_id)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->ed_v1_arbeitgeberlogo_hash_id_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**ed_v1_arbeitgeberlogo_hash_id_get**](docs/DefaultApi.md#ed_v1_arbeitgeberlogo_hash_id_get) | **GET** /ed/v1/arbeitgeberlogo/{hashID} | Unternehmen Logo
*DefaultApi* | [**pc_v1_app_jobs_hash_id_bewerbung_get**](docs/DefaultApi.md#pc_v1_app_jobs_hash_id_bewerbung_get) | **GET** /pc/v1/app/jobs/{hashID}/bewerbung | Bewerbung Kontaktdaten
*DefaultApi* | [**pc_v1_jobdetails_hash_id_get**](docs/DefaultApi.md#pc_v1_jobdetails_hash_id_get) | **GET** /pc/v1/jobdetails/{hashID} | Jobdetail
*DefaultApi* | [**pc_v2_app_jobs_get**](docs/DefaultApi.md#pc_v2_app_jobs_get) | **GET** /pc/v2/app/jobs/ | Jobsuche


## Documentation For Models

 - [JobApplicationDetails](docs/JobApplicationDetails.md)
 - [JobApplicationDetailsAngebotskontakt](docs/JobApplicationDetailsAngebotskontakt.md)
 - [JobApplicationDetailsAngebotskontaktFestnetznummer](docs/JobApplicationDetailsAngebotskontaktFestnetznummer.md)
 - [JobApplicationDetailsAngebotskontaktMobilnummer](docs/JobApplicationDetailsAngebotskontaktMobilnummer.md)
 - [JobDetails](docs/JobDetails.md)
 - [JobDetailsArbeitgeberAdresse](docs/JobDetailsArbeitgeberAdresse.md)
 - [JobDetailsArbeitsorte](docs/JobDetailsArbeitsorte.md)
 - [JobDetailsAusbildungen](docs/JobDetailsAusbildungen.md)
 - [JobDetailsFertigkeiten](docs/JobDetailsFertigkeiten.md)
 - [JobDetailsFuehrungskompetenzen](docs/JobDetailsFuehrungskompetenzen.md)
 - [JobDetailsKoordinaten](docs/JobDetailsKoordinaten.md)
 - [JobDetailsLinks](docs/JobDetailsLinks.md)
 - [JobDetailsLinksArbeitgeberlogo](docs/JobDetailsLinksArbeitgeberlogo.md)
 - [JobDetailsLinksBewerbung](docs/JobDetailsLinksBewerbung.md)
 - [JobDetailsLinksDetails](docs/JobDetailsLinksDetails.md)
 - [JobDetailsLinksSelf](docs/JobDetailsLinksSelf.md)
 - [JobDetailsMobilitaet](docs/JobDetailsMobilitaet.md)
 - [JobDetailsSprachkenntnisse](docs/JobDetailsSprachkenntnisse.md)
 - [JobSearchResponse](docs/JobSearchResponse.md)
 - [JobSearchResponseAggregierungen](docs/JobSearchResponseAggregierungen.md)
 - [JobSearchResponseAggregierungenBundesland](docs/JobSearchResponseAggregierungenBundesland.md)
 - [JobSearchResponseAggregierungenPlzebene2](docs/JobSearchResponseAggregierungenPlzebene2.md)
 - [JobSearchResponseAuswahl](docs/JobSearchResponseAuswahl.md)
 - [JobSearchResponseEmbedded](docs/JobSearchResponseEmbedded.md)
 - [JobSearchResponseEmbeddedArbeitsort](docs/JobSearchResponseEmbeddedArbeitsort.md)
 - [JobSearchResponseEmbeddedArbeitsortKoordinaten](docs/JobSearchResponseEmbeddedArbeitsortKoordinaten.md)
 - [JobSearchResponseEmbeddedJobs](docs/JobSearchResponseEmbeddedJobs.md)
 - [JobSearchResponseEmbeddedLinks](docs/JobSearchResponseEmbeddedLinks.md)
 - [JobSearchResponseEmbeddedLinksArbeitgeberlogo](docs/JobSearchResponseEmbeddedLinksArbeitgeberlogo.md)
 - [JobSearchResponseEmbeddedLinksDetails](docs/JobSearchResponseEmbeddedLinksDetails.md)
 - [JobSearchResponseEmbeddedLinksJobdetails](docs/JobSearchResponseEmbeddedLinksJobdetails.md)
 - [JobSearchResponseFacetten](docs/JobSearchResponseFacetten.md)
 - [JobSearchResponseLinks](docs/JobSearchResponseLinks.md)
 - [JobSearchResponseLinksFirst](docs/JobSearchResponseLinksFirst.md)
 - [JobSearchResponseLinksLast](docs/JobSearchResponseLinksLast.md)
 - [JobSearchResponseLinksNext](docs/JobSearchResponseLinksNext.md)
 - [JobSearchResponseLinksSelf](docs/JobSearchResponseLinksSelf.md)
 - [JobSearchResponsePage](docs/JobSearchResponsePage.md)
 - [JobSearchResponseParserResult](docs/JobSearchResponseParserResult.md)
 - [JobSearchResponseParserResultKoordinaten](docs/JobSearchResponseParserResultKoordinaten.md)


## Documentation For Authorization


## clientCredAuth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in jobsuche.apis and jobsuche.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from deutschland.jobsuche.api.default_api import DefaultApi`
- `from deutschland.jobsuche.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
from deutschland import jobsuche
from deutschland.jobsuche.apis import *
from deutschland.jobsuche.models import *
```
