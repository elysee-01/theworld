from datapackage import Package
from .models import Country
from continent.models import Continent


def run():
    package = Package('https://datahub.io/core/country-codes/datapackage.json')
    # print(package.get_resource('country-codes_csv').read())
    # print(package.get_resource('country-codes_json').read())
    # print(package.get_resource('country-codes').read())
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            for line in resource.read(keyed=True):

                iso = line.get('ISO3166-1-Alpha-2')
                code = line.get('Continent')

                print(iso, '||', code)

                continent = Continent.objects.filter(code=code).first()
                country = Country.objects.filter(iso=iso).first()

                if not continent:
                    continent = Continent()
                    continent.code = code
                    continent.save()

                if not country:
                    country = Country()
                    country.telephone_prefix = line.get('Dial')
                    country.fr_name = line.get('official_name_fr')
                    country.en_name = line.get('official_name_en')
                    country.iso3 = line.get('ISO3166-1-Alpha-3')
                    country.iso = iso
                    country.name = line.get('ISO4217-currency_country_name')
                    country.continent = continent
                    # country.capital = line.get('Capital')
                    country.save()

