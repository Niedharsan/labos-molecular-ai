from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, Field


class MolecularTaskType(StrEnum):
    CLONING = "cloning"
    KNOCKOUT = "knockout"
    KNOCKIN = "knockin"
    GENERAL = "general"


class CompletionRequirement(BaseModel):
    id: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=3, max_length=1000)


class CompletionContract(BaseModel):
    task_type: MolecularTaskType
    completion_level: Literal[
        "strategy",
        "design",
        "executable_design",
        "protocol",
    ] = "executable_design"
    required_outputs: list[CompletionRequirement]
