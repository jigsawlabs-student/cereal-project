from dagster import Definitions

from cereal_project.assets.cereal import (cereals, highest_calorie_cereal,
                                          highest_protein_cereal)
from cereal_project.jobs import hello_cereal_job

defs = Definitions(
    assets=[cereals, highest_calorie_cereal, highest_protein_cereal],
    jobs=[hello_cereal_job]
)