import matplotlib as mpl


def apply_portfolio_theme(font_family: str = "Segoe UI"):
    mpl.rcParams.update({
        "font.family": font_family,
        "font.size": 10,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,

        "figure.dpi": 110,
        "savefig.dpi": 180,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.15,

        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.28,
        "axes.spines.top": True,
        "axes.spines.right": True,

        "xtick.labelsize": 10,
        "ytick.labelsize": 10,

        "legend.frameon": True,
        "legend.framealpha": 0.95,
        "legend.fontsize": 10,
        "legend.title_fontsize": 10,

        "axes.unicode_minus": False,
    })
