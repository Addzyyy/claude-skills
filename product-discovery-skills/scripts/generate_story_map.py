#!/usr/bin/env python3
"""
Generate a visual user story map as a standalone HTML file.

Usage:
    python generate_story_map.py story-map.json [output.html]

Input JSON format:
{
  "title": "Project Name",
  "personas": ["Persona 1", "Persona 2"],
  "activities": [
    {
      "name": "Activity Name",
      "stories": [
        {"text": "Story text", "persona": "Persona 1", "slice": 1},
        {"text": "Another story", "persona": "Persona 2", "slice": 2}
      ]
    }
  ],
  "slices": [
    {"name": "Walking Skeleton", "color": "#e8f5e9"},
    {"name": "Release 2", "color": "#e3f2fd"},
    {"name": "Release 3", "color": "#fff3e0"}
  ]
}

Stories are assigned to slices by the "slice" field (1-indexed).
Slice 0 or missing = unassigned (shown at bottom).
"""

import json
import sys
from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Story Map</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #f5f5f5;
    padding: 24px;
    color: #333;
  }}
  h1 {{
    font-size: 1.5rem;
    margin-bottom: 8px;
  }}
  .personas {{
    font-size: 0.85rem;
    color: #666;
    margin-bottom: 20px;
  }}
  .personas span {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 12px;
    margin-right: 6px;
    font-weight: 500;
  }}
  .map-container {{
    overflow-x: auto;
    padding-bottom: 20px;
  }}
  .story-map {{
    display: grid;
    grid-template-columns: 120px {col_template};
    gap: 0;
    min-width: max-content;
  }}
  .backbone-header {{
    background: #1a237e;
    color: white;
    padding: 12px 16px;
    font-weight: 600;
    font-size: 0.95rem;
    text-align: center;
    border: 1px solid #0d1642;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .slice-label {{
    padding: 8px 12px;
    font-weight: 600;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    border-left: 3px solid #999;
    writing-mode: horizontal-tb;
    min-height: 80px;
  }}
  .story-cell {{
    padding: 6px;
    min-height: 80px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    border-right: 1px dashed #ddd;
  }}
  .story-card {{
    background: white;
    border-radius: 6px;
    padding: 10px 12px;
    font-size: 0.82rem;
    line-height: 1.4;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-left: 3px solid #ccc;
    cursor: default;
  }}
  .story-card:hover {{
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }}
  .story-card .persona-tag {{
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    margin-bottom: 4px;
  }}
  .corner {{
    background: #f5f5f5;
  }}
  .slice-row {{
    display: contents;
  }}
  .legend {{
    margin-top: 20px;
    font-size: 0.8rem;
    color: #666;
  }}
  .legend-item {{
    display: inline-flex;
    align-items: center;
    margin-right: 16px;
  }}
  .legend-swatch {{
    width: 14px;
    height: 14px;
    border-radius: 3px;
    margin-right: 6px;
    border: 1px solid rgba(0,0,0,0.1);
  }}
</style>
</head>
<body>

<h1>{title} — User Story Map</h1>
<div class="personas">Personas: {persona_tags}</div>

<div class="map-container">
<div class="story-map">
  {grid_content}
</div>
</div>

<div class="legend">
  {legend}
</div>

</body>
</html>"""

PERSONA_COLORS = [
    "#2196F3", "#4CAF50", "#FF9800", "#9C27B0", "#F44336",
    "#00BCD4", "#795548", "#607D8B", "#E91E63", "#3F51B5"
]

DEFAULT_SLICE_COLORS = [
    "#e8f5e9", "#e3f2fd", "#fff3e0", "#fce4ec", "#f3e5f5",
    "#e0f7fa", "#fff8e1", "#e8eaf6"
]


def generate_html(data: dict) -> str:
    title = data.get("title", "Story Map")
    personas = data.get("personas", [])
    activities = data.get("activities", [])
    slices = data.get("slices", [])

    # Assign colors to personas
    persona_color_map = {}
    for i, p in enumerate(personas):
        persona_color_map[p] = PERSONA_COLORS[i % len(PERSONA_COLORS)]

    # Assign default colors to slices if missing
    for i, s in enumerate(slices):
        if "color" not in s:
            s["color"] = DEFAULT_SLICE_COLORS[i % len(DEFAULT_SLICE_COLORS)]

    num_activities = len(activities)
    col_template = " ".join(["minmax(180px, 1fr)"] * num_activities)

    # Build persona tags
    persona_tags = " ".join(
        f'<span style="background:{persona_color_map.get(p, "#ccc")}20;'
        f'color:{persona_color_map.get(p, "#333")}">{p}</span>'
        for p in personas
    )

    # Build grid content
    lines = []

    # Header row: corner + activity names
    lines.append('<div class="backbone-header corner">Releases</div>')
    for act in activities:
        lines.append(f'<div class="backbone-header">{act["name"]}</div>')

    # One row per slice
    for si, sl in enumerate(slices):
        slice_num = si + 1
        bg = sl["color"]

        # Slice label
        lines.append(
            f'<div class="slice-label" style="background:{bg}">'
            f'{sl["name"]}</div>'
        )

        # One cell per activity
        for act in activities:
            stories_in_cell = [
                s for s in act.get("stories", [])
                if s.get("slice", 0) == slice_num
            ]
            lines.append(f'<div class="story-cell" style="background:{bg}">')
            for story in stories_in_cell:
                persona = story.get("persona", "")
                border_color = persona_color_map.get(persona, "#ccc")
                tag_color = persona_color_map.get(persona, "#666")
                persona_tag = (
                    f'<div class="persona-tag" style="color:{tag_color}">'
                    f'{persona}</div>'
                    if persona else ""
                )
                lines.append(
                    f'<div class="story-card" style="border-left-color:{border_color}">'
                    f'{persona_tag}{story["text"]}</div>'
                )
            lines.append("</div>")

    grid_content = "\n  ".join(lines)

    # Legend
    legend_items = []
    for p in personas:
        c = persona_color_map.get(p, "#ccc")
        legend_items.append(
            f'<span class="legend-item">'
            f'<span class="legend-swatch" style="background:{c}"></span>'
            f'{p}</span>'
        )
    legend = " ".join(legend_items)

    return TEMPLATE.format(
        title=title,
        col_template=col_template,
        persona_tags=persona_tags,
        grid_content=grid_content,
        legend=legend,
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_story_map.py <input.json> [output.html]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".html")

    with open(input_path) as f:
        data = json.load(f)

    html = generate_html(data)

    with open(output_path, "w") as f:
        f.write(html)

    print(f"Story map generated: {output_path}")


if __name__ == "__main__":
    main()
