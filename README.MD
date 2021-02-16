```PYTHON

    # https://datahub.io/core/country-codes/r/country-codes.json

    from datapackage import Package

    package = Package('https://datahub.io/core/country-codes/r/country-codes.json')

    # print list of all resources:
    print(package.resource_names)

    # print processed tabular data (if exists any)
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            print(resource.read())

```
from django_countries.fields import Country
from country import models

cnt = models.Country.objects.all()
for c in cnt:
    p = Country(code=c.iso)
    if p.name and p.alpha3:
            c.drapeau = p.flag.lstrip('/static/')
            c.save()
