from pathlib import Path

SAVE_ARTIFACTS = False

ARTIFACT_DIR = Path("modelling") / "outputs" / "latest"


def maybe_mkdir(p: Path):
    if SAVE_ARTIFACTS:
        p.mkdir(parents=True, exist_ok=True)


def maybe_savefig(fig, path: Path, dpi=200):
    if SAVE_ARTIFACTS:
        maybe_mkdir(path.parent)
        fig.savefig(path, dpi=dpi, bbox_inches="tight")


def maybe_to_csv(df, path: Path, index=False):
    if SAVE_ARTIFACTS:
        maybe_mkdir(path.parent)
        df.to_csv(path, index=index)
