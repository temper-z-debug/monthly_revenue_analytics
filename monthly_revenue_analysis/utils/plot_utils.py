import matplotlib.pyplot as plt

def add_takeaway(ax, text: str):
    fig = ax.figure
    fig.text(
        0.01, 0.02,
        f"Takeaway: {text}",
        ha="left",
        va="bottom",
        fontsize=10,
        bbox=dict(
            boxstyle="round,pad=0.30",
            facecolor="white",
            alpha=0.90,
            edgecolor="none"
        )
    )


def add_footer_note(fig, text: str, y: float = 0.02):
    fig.text(
        0.01, y, text,
        ha="left", va="bottom",
        fontsize=9
    )


def reserve_footer_space(fig, bottom: float = 0.20):
    fig.subplots_adjust(bottom=bottom)
