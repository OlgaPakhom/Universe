import pytest
from random import randint
from inheritance import Car
from inheritance import Star
from inheritance import Planet

@pytest.mark.parametrize('mass', [randint(0,1000) for x in range(5)])
@pytest.mark.parametrize('density', [randint(0,100) for y in range(5)])
@pytest.mark.parametrize('radius', [randint(0,1000) for y in range(5)])

class TestCar:
    names = ['Roadster', 'ModelS', 'SpaceX', 'Model3']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_car_name_positive(self, name_expected, mass, density, radius):
        tesla = Car(name_expected, mass, density,[], radius)
        assert car.name == name_expected
 
    @pytest.mark.xfail(raises=NameError)
    def test_car_name_whitespace_negative(self, mass, density, radius):
        name_not_alnum = 'Tesla-Roadster'

@pytest.mark.parametrize('mass', [randint(0,9000000) for x in range(5)])
@pytest.mark.parametrize('density', [randint(0,9000000) for y in range(5)])
@pytest.mark.parametrize('radius', [randint(0,9000000) for y in range(5)])

class TestStar:
    names = ['Polaris', 'Sirius', 'Vega']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_star_name_positive(self, name_expected, mass, density, radius):
        stars = Star(name_expected, mass, density,[], radius)
        assert stars.name == name_expected
        
    names_not_alnum = ['Ve-ga', 'Star@', 'Polar+is', "Siri'us"] 
    @pytest.mark.xfail(raises=NameError)
    @pytest.mark.parametrize(('name_not_alnum'), names_not_alnum)
    def test_star_name_negative(self, name_not_alnum, mass, density, radius):
         name_not_alnum = 'Ve-ga' 
			
@pytest.mark.parametrize('mass', [randint(0,100000) for x in range(5)])
@pytest.mark.parametrize('density', [randint(0,100000) for y in range(5)])
@pytest.mark.parametrize('radius', [randint(0,100000) for y in range(5)])

class TestPlanet:
    names = ['Earth', 'Mars', 'Uranus']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_planet_name_positive(self, name_expected, mass, density, radius):
        planets = Planet(name_expected, mass, density,[], radius, 1)
        assert planets.name == name_expected
        
    names_not_alnum = ['Ea%rth', 'Ma-rs', 'Uranu<s', "Jupi'ter"]  
    @pytest.mark.xfail(raises=NameError)
    @pytest.mark.parametrize(('name_not_alnum'), names_not_alnum)
    def test_planet_name_negative(self, name_not_alnum, mass, density, radius):
         name_not_alnum = 'E[arth'
