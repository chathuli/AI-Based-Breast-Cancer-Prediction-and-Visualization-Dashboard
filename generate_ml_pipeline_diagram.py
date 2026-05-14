"""
Generate ML Pipeline Flow Diagrams for Chapter 5.3
Creates professional flow diagrams showing the complete ML pipeline
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

def create_ml_pipeline_diagram(output_dir):
    """Create comprehensive ML pipeline flow diagram"""
    print("\n📊 Generating ML Pipeline Flow Diagram...")
    
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Title
    ax.text(5, 13.5, 'ML Pipeline Architecture', 
            ha='center', fontsize=20, fontweight='bold')
    
    # Define colors
    color_input = '#FFE5B4'
    color_process = '#B4D7FF'
    color_model = '#FFB4B4'
    color_output = '#B4FFB4'
    color_explain = '#E5B4FF'
    
    # Helper function to create boxes
    def create_box(x, y, width, height, text, color, fontsize=11):
        box = FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.1", 
            edgecolor='black', facecolor=color,
            linewidth=2, zorder=2
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', 
                fontsize=fontsize, fontweight='bold', zorder=3)
    
    # Helper function to create arrows
    def create_arrow(x1, y1, x2, y2, label='', style='->'):
        arrow = FancyArrowPatch(
            (x1, y1), (x2, y2),
            arrowstyle=style, mutation_scale=20,
            linewidth=2, color='black', zorder=1
        )
        ax.add_patch(arrow)
        if label:
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mid_x + 0.3, mid_y, label, fontsize=9, 
                    style='italic', bbox=dict(boxstyle='round', 
                    facecolor='white', alpha=0.8))
    
    # 1. Raw Input
    create_box(5, 12, 2, 0.6, 'Raw Input\n(30 Features)', color_input, 12)
    
    # Arrow to validation
    create_arrow(5, 11.7, 5, 11.2)
    
    # 2. Input Validation
    create_box(5, 10.8, 2.5, 0.6, 'Input Validation\n(Check ranges & types)', 
               color_process, 11)
    
    # Arrow to preprocessing
    create_arrow(5, 10.5, 5, 10)
    
    # 3. Preprocessing
    create_box(5, 9.6, 2.5, 0.6, 'Data Preprocessing\n(Handle missing values)', 
               color_process, 11)
    
    # Arrow to scaler
    create_arrow(5, 9.3, 5, 8.8)
    
    # 4. StandardScaler
    create_box(5, 8.4, 2.5, 0.6, 'StandardScaler\n(Normalize features)', 
               color_process, 11)
    
    # Arrows to three models (parallel)
    create_arrow(5, 8.1, 2, 7.2, 'Scaled\nData')
    create_arrow(5, 8.1, 5, 7.2, 'Scaled\nData')
    create_arrow(5, 8.1, 8, 7.2, 'Scaled\nData')
    
    # 5. Three Models (Parallel)
    create_box(2, 6.5, 2, 0.8, 'Logistic\nRegression', color_model, 11)
    create_box(5, 6.5, 2, 0.8, 'Decision\nTree', color_model, 11)
    create_box(8, 6.5, 2, 0.8, 'SVM\n(Best Model)', color_model, 11)
    
    # Model outputs
    ax.text(2, 5.9, 'Prediction\n+ Probability', ha='center', fontsize=9, style='italic')
    ax.text(5, 5.9, 'Prediction\n+ Probability', ha='center', fontsize=9, style='italic')
    ax.text(8, 5.9, 'Prediction\n+ Probability', ha='center', fontsize=9, style='italic')
    
    # Arrows to ensemble
    create_arrow(2, 6.1, 5, 5.2)
    create_arrow(5, 6.1, 5, 5.2)
    create_arrow(8, 6.1, 5, 5.2)
    
    # 6. Enhanced Predictor (Ensemble)
    create_box(5, 4.6, 3, 0.8, 'Enhanced Predictor\n(Ensemble & Voting)', 
               color_process, 11)
    
    # Arrow to SHAP
    create_arrow(5, 4.2, 5, 3.6)
    
    # 7. SHAP Explainer
    create_box(5, 3.2, 2.5, 0.6, 'SHAP Explainer\n(Feature Importance)', 
               color_explain, 11)
    
    # Arrow to output processing
    create_arrow(5, 2.9, 5, 2.4)
    
    # 8. Output Processing
    create_box(5, 2, 2.5, 0.6, 'Output Processing\n(Format results)', 
               color_process, 11)
    
    # Arrow to final output
    create_arrow(5, 1.7, 5, 1.2)
    
    # 9. Final Output
    create_box(5, 0.6, 3.5, 0.8, 'Final Output\n(Diagnosis + Confidence + Explanations)', 
               color_output, 11)
    
    # Add legend
    legend_elements = [
        mpatches.Patch(facecolor=color_input, edgecolor='black', label='Input'),
        mpatches.Patch(facecolor=color_process, edgecolor='black', label='Processing'),
        mpatches.Patch(facecolor=color_model, edgecolor='black', label='ML Models'),
        mpatches.Patch(facecolor=color_explain, edgecolor='black', label='Explainability'),
        mpatches.Patch(facecolor=color_output, edgecolor='black', label='Output')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10, 
              frameon=True, shadow=True)
    
    # Add annotations
    ax.text(0.5, 0.2, 'Pipeline Flow: Top to Bottom', 
            fontsize=10, style='italic', 
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'ml_pipeline_flow_diagram.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def create_detailed_pipeline_diagram(output_dir):
    """Create detailed ML pipeline with all components"""
    print("\n📊 Generating Detailed Pipeline Diagram...")
    
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    ax.text(6, 15.5, 'Detailed ML Pipeline Architecture', 
            ha='center', fontsize=22, fontweight='bold')
    
    # Colors
    colors = {
        'input': '#FFE5B4',
        'validation': '#B4D7FF',
        'preprocessing': '#B4E5FF',
        'scaling': '#B4FFE5',
        'model': '#FFB4B4',
        'ensemble': '#FFD7B4',
        'explainer': '#E5B4FF',
        'output': '#B4FFB4'
    }
    
    def box(x, y, w, h, text, color, fs=10):
        rect = FancyBboxPatch((x-w/2, y-h/2), w, h,
                              boxstyle="round,pad=0.08",
                              edgecolor='black', facecolor=color,
                              linewidth=2.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center',
                fontsize=fs, fontweight='bold', zorder=3)
    
    def arrow(x1, y1, x2, y2, label=''):
        arr = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2.5, color='black', zorder=1)
        ax.add_patch(arr)
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx+0.4, my, label, fontsize=8, style='italic',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Layer 1: Input
    box(6, 14.5, 3, 0.7, 'User Input\n30 Numerical Features', colors['input'], 11)
    arrow(6, 14.15, 6, 13.6)
    
    # Layer 2: Validation
    box(6, 13.2, 3.5, 0.7, 'Input Validation Layer', colors['validation'], 11)
    box(3, 12.3, 2.5, 0.5, 'Range Check\n(0-100)', colors['validation'], 9)
    box(6, 12.3, 2.5, 0.5, 'Type Check\n(Numeric)', colors['validation'], 9)
    box(9, 12.3, 2.5, 0.5, 'Missing Value\nCheck', colors['validation'], 9)
    
    arrow(6, 12.85, 3, 12.55)
    arrow(6, 12.85, 6, 12.55)
    arrow(6, 12.85, 9, 12.55)
    arrow(3, 12.05, 6, 11.5)
    arrow(6, 12.05, 6, 11.5)
    arrow(9, 12.05, 6, 11.5)
    
    # Layer 3: Preprocessing
    box(6, 11.1, 3.5, 0.7, 'Preprocessing Layer', colors['preprocessing'], 11)
    box(3.5, 10.2, 2.2, 0.5, 'Handle\nMissing', colors['preprocessing'], 9)
    box(6, 10.2, 2.2, 0.5, 'Remove\nOutliers', colors['preprocessing'], 9)
    box(8.5, 10.2, 2.2, 0.5, 'Feature\nSelection', colors['preprocessing'], 9)
    
    arrow(6, 10.75, 3.5, 10.45)
    arrow(6, 10.75, 6, 10.45)
    arrow(6, 10.75, 8.5, 10.45)
    arrow(3.5, 9.95, 6, 9.4)
    arrow(6, 9.95, 6, 9.4)
    arrow(8.5, 9.95, 6, 9.4)
    
    # Layer 4: Scaling
    box(6, 9, 3, 0.7, 'StandardScaler\nμ=0, σ=1', colors['scaling'], 11)
    arrow(6, 8.65, 3, 7.9, '30 features')
    arrow(6, 8.65, 6, 7.9, '30 features')
    arrow(6, 8.65, 9, 7.9, '30 features')
    
    # Layer 5: Models
    ax.text(6, 7.5, 'Model Layer (Parallel Processing)', 
            ha='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.5))
    
    box(3, 6.7, 2.3, 0.9, 'Logistic\nRegression\nModel', colors['model'], 10)
    box(6, 6.7, 2.3, 0.9, 'Decision Tree\nClassifier\nModel', colors['model'], 10)
    box(9, 6.7, 2.3, 0.9, 'Support Vector\nMachine\n(RBF Kernel)', colors['model'], 10)
    
    # Model details
    ax.text(3, 6.0, 'Linear\nmax_iter=10000', ha='center', fontsize=8, style='italic')
    ax.text(6, 6.0, 'max_depth=5\nrandom_state=42', ha='center', fontsize=8, style='italic')
    ax.text(9, 6.0, 'C=1.0, γ=auto\nrandom_state=42', ha='center', fontsize=8, style='italic')
    
    arrow(3, 6.25, 6, 5.4, 'Pred +\nProba')
    arrow(6, 6.25, 6, 5.4, 'Pred +\nProba')
    arrow(9, 6.25, 6, 5.4, 'Pred +\nProba')
    
    # Layer 6: Ensemble
    box(6, 4.9, 3.5, 0.8, 'Enhanced Predictor\n(Ensemble Voting)', colors['ensemble'], 11)
    box(3.5, 4.0, 2, 0.5, 'Soft Voting', colors['ensemble'], 9)
    box(6, 4.0, 2, 0.5, 'Confidence\nAggregation', colors['ensemble'], 9)
    box(8.5, 4.0, 2, 0.5, 'Best Model\nSelection', colors['ensemble'], 9)
    
    arrow(6, 4.5, 3.5, 4.25)
    arrow(6, 4.5, 6, 4.25)
    arrow(6, 4.5, 8.5, 4.25)
    arrow(3.5, 3.75, 6, 3.2)
    arrow(6, 3.75, 6, 3.2)
    arrow(8.5, 3.75, 6, 3.2)
    
    # Layer 7: SHAP
    box(6, 2.8, 3, 0.7, 'SHAP Explainer', colors['explainer'], 11)
    box(3.5, 1.9, 2, 0.5, 'Feature\nImportance', colors['explainer'], 9)
    box(6, 1.9, 2, 0.5, 'SHAP\nValues', colors['explainer'], 9)
    box(8.5, 1.9, 2, 0.5, 'Force Plot\nGeneration', colors['explainer'], 9)
    
    arrow(6, 2.45, 3.5, 2.15)
    arrow(6, 2.45, 6, 2.15)
    arrow(6, 2.45, 8.5, 2.15)
    arrow(3.5, 1.65, 6, 1.1)
    arrow(6, 1.65, 6, 1.1)
    arrow(8.5, 1.65, 6, 1.1)
    
    # Layer 8: Output
    box(6, 0.6, 4, 0.8, 'Final Output\nDiagnosis + Confidence + Explanations + Report', 
        colors['output'], 11)
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'detailed_ml_pipeline_diagram.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def create_horizontal_pipeline_diagram(output_dir):
    """Create horizontal flow diagram"""
    print("\n📊 Generating Horizontal Pipeline Diagram...")
    
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(10, 7.5, 'ML Pipeline - Horizontal Flow', 
            ha='center', fontsize=20, fontweight='bold')
    
    # Define stages
    stages = [
        (1, 'Raw\nInput', '#FFE5B4'),
        (3, 'Validation', '#B4D7FF'),
        (5, 'Standard\nScaler', '#B4FFE5'),
        (7, 'Logistic\nRegression', '#FFB4B4'),
        (9, 'Decision\nTree', '#FFB4B4'),
        (11, 'SVM\n(Best)', '#FFB4B4'),
        (13, 'Enhanced\nPredictor', '#FFD7B4'),
        (15, 'SHAP\nExplainer', '#E5B4FF'),
        (17, 'Output', '#B4FFB4'),
        (19, 'Report', '#B4FFB4')
    ]
    
    def box(x, text, color):
        rect = FancyBboxPatch((x-0.7, 3.5), 1.4, 1.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='black', facecolor=color,
                              linewidth=2, zorder=2)
        ax.add_patch(rect)
        ax.text(x, 4.25, text, ha='center', va='center',
                fontsize=10, fontweight='bold', zorder=3)
    
    def arrow(x1, x2):
        arr = FancyArrowPatch((x1, 4.25), (x2, 4.25),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='black', zorder=1)
        ax.add_patch(arr)
    
    # Draw stages
    for i, (x, text, color) in enumerate(stages):
        box(x, text, color)
        if i < len(stages) - 1:
            arrow(x + 0.7, stages[i+1][0] - 0.7)
    
    # Add parallel processing indicator
    ax.plot([6.3, 11.7], [2.5, 2.5], 'k--', linewidth=2)
    ax.text(9, 2.2, 'Parallel Processing', ha='center', fontsize=10, style='italic')
    
    # Add stage numbers
    for i, (x, _, _) in enumerate(stages, 1):
        ax.text(x, 5.3, f'Stage {i}', ha='center', fontsize=8, 
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'horizontal_ml_pipeline_diagram.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def main():
    """Main function"""
    
    print("\n" + "="*80)
    print("ML PIPELINE FLOW DIAGRAMS - CHAPTER 5.3")
    print("="*80)
    
    # Create output directory
    output_dir = 'ml_pipeline_diagrams'
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n📁 Output directory: {output_dir}/")
    
    # Generate diagrams
    create_ml_pipeline_diagram(output_dir)
    create_detailed_pipeline_diagram(output_dir)
    create_horizontal_pipeline_diagram(output_dir)
    
    print("\n" + "="*80)
    print("✅ ALL PIPELINE DIAGRAMS GENERATED!")
    print("="*80)
    print(f"\n📂 Files saved in: {os.path.abspath(output_dir)}/")
    print("\n📊 Generated files:")
    print("   1. ml_pipeline_flow_diagram.png - Simple vertical flow")
    print("   2. detailed_ml_pipeline_diagram.png - Detailed with all components")
    print("   3. horizontal_ml_pipeline_diagram.png - Horizontal flow view")
    print("\n🎯 Use these in your Chapter 5.3!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
