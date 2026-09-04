from dataclasses import dataclass
from pathlib import Path

from app.services.crispr_agents.molecular_models import MolecularTaskType


@dataclass(frozen=True)
class SkillDocument:
    name: str
    path: Path
    content: str


class SkillRegistry:
    """Read-only loader for repository-controlled molecular reasoning skills."""

    def __init__(self, root: Path | None = None):
        self.root = root or Path(__file__).resolve().parents[2] / "agent_skills"

    def load(self, name: str) -> SkillDocument:
        safe_name = name.strip().replace("..", "")
        path = self.root / safe_name / "SKILL.md"
        if not path.is_file():
            raise FileNotFoundError(f"Molecular skill not found: {safe_name}")
        return SkillDocument(
            name=safe_name,
            path=path,
            content=path.read_text(encoding="utf-8"),
        )

    def names_for_task(self, task_type: MolecularTaskType) -> list[str]:
        names = ["molecular-core"]
        if task_type == MolecularTaskType.CLONING:
            names.append("cloning")
        elif task_type == MolecularTaskType.KNOCKIN:
            names.extend(["knockin", "cloning"])
        elif task_type == MolecularTaskType.KNOCKOUT:
            names.append("knockout")
        return names

    def names_for_tasks(self, task_types: list[MolecularTaskType]) -> list[str]:
        names: list[str] = []
        for task_type in task_types:
            for name in self.names_for_task(task_type):
                if name not in names:
                    names.append(name)
        return names
