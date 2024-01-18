--Select *
--From PortfolioProject.dbo.CovidDeaths
--order by 3,4


--Select * 
--From PortfolioProject.dbo.CovidVaccinations
--order by 3,4

--Looking at Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in Germany

Select Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
From PortfolioProject..CovidDeaths
Where location = 'Germany'
order by 1,2

-- Looking at Total Cases vs Population
-- Shows what percentage of population got Covid at least once

Select Location, date, total_cases, population, (total_cases/population)*100 as CovidPercentage
From PortfolioProject..CovidDeaths
order by 1,2

-- Looking at Countries with highest Infection Rate compared to Population

Select Location, Population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population)*100) as PercentPopulationInfected
from PortfolioProject..CovidDeaths
group by Location, Population
order by PercentPopulationInfected DESC

-- Showing Countries with highest Death Count

Select Location, MAX(cast(total_deaths as int)) as TotalDeathCount
from PortfolioProject..CovidDeaths
Where continent is not null
group by location
order by TotalDeathCount DESC

-- Showing Continents with highest Death Count

Select Location, MAX(cast(total_deaths as int)) as TotalDeathCount
from PortfolioProject..CovidDeaths
Where continent is null
group by location
order by TotalDeathCount DESC

-- GLOBAL NUMBERS

Select Sum(new_cases) as total_cases, Sum(cast(new_deaths as int)) as total_deaths, Sum(cast(new_deaths as int))/Nullif (Sum(new_cases),0)*100 as DeathPercentage
From PortfolioProject..CovidDeaths

-- Looking at Total Population vs Vaccinations

Drop Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric)

Insert into #PercentPopulationVaccinated
Select CD.continent, CD.location, CD.date, CD.population, CV.new_vaccinations,
 Sum(Convert(int,CV.new_vaccinations)) OVER (Partition by CD.location ORDER BY CD.location, CD.date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths CD
Join PortfolioProject..CovidVaccinations CV
	On CD.location = CV.location 
	and CD.date = CV.date
Where CD.continent is not null

Select *, (RollingPeopleVaccinated/population)*100
From #PercentPopulationVaccinated

-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinated as
Select CD.continent, CD.location, CD.date, CD.population, CV.new_vaccinations,
 Sum(Convert(int,CV.new_vaccinations)) OVER (Partition by CD.location ORDER BY CD.location, CD.date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths CD
Join PortfolioProject..CovidVaccinations CV
	On CD.location = CV.location 
	and CD.date = CV.date
Where CD.continent is not null
