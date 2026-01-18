from pathlib import Path

# ===== 默认：调试阶段不落盘 =====
SAVE_ARTIFACTS = False

# 固定覆盖目录（推荐：永远只有一份最新结果）
# 注意：这里是相对“项目根目录”的路径
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
