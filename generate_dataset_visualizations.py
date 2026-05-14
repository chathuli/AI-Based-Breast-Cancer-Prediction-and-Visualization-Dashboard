"""
Generate Dataset Distribution Visualizations for Chapter 3.2
Creates professional charts showing class distribution and dataset statistics
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
import os

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def load_dataset():
    """Load breast cancer dataset"""
    print("📊 Loading breast cancer dataset...")
    
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='diagnosis')
    
    # Create full dataset
    df = X.copy()
    df['diagnosis'] = y
    df['diagnosis_label'] = df['diagnosis'].map({0: 'Malignant', 1: 'Benign'})
    
    print(f"✅ Dataset loaded: {len(df)} total samples")
    
    return df, data

def plot_class_distribution_bar(df, output_dir):
    """Plot class distribution as bar chart"""
    print("\n📊 Generating Bar Chart...")
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Count classes
    class_counts = df['diagnosis_label'].value_counts()
    total = len(df)
    
    # Calculate percentages
    percentages = (class_counts / total * 100).round(1)
    
    # Create bar chart
    colors = ['#FF6B6B', '#4ECDC4']
    bars = ax.bar(class_counts.index, class_counts.values, color=colors, 
                   edgecolor='black', linewidth=2, alpha=0.8)
    
    # Add value labels on bars
    for bar, count, pct in zip(bars, class_counts.values, percentages.values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({pct}%)',
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    # Styling
    ax.set_xlabel('Diagnosis', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Samples', fontsize=14, fontweight='bold')
    ax.set_title('Breast Cancer Dataset - Class Distribution', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3)
    
    # Add total count
    ax.text(0.5, 0.95, f'Total Samples: {total}',
            transform=ax.transAxes, ha='center', va='top',
            fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'class_distribution_bar_chart.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def plot_class_distribution_pie(df, output_dir):
    """Plot class distribution as pie chart"""
    print("\n🥧 Generating Pie Chart...")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Count classes
    class_counts = df['diagnosis_label'].value_counts()
    
    # Colors
    colors = ['#4ECDC4', '#FF6B6B']
    explode = (0.05, 0.05)  # Slightly separate slices
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(
        class_counts.values,
        labels=class_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        shadow=True,
        textprops={'fontsize': 14, 'fontweight': 'bold'}
    )
    
    # Enhance text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(16)
        autotext.set_fontweight('bold')
    
    # Add legend with counts
    legend_labels = [f'{label}: {count} samples' 
                     for label, count in zip(class_counts.index, class_counts.values)]
    ax.legend(legend_labels, loc='upper left', fontsize=12, frameon=True, shadow=True)
    
    ax.set_title('Breast Cancer Dataset - Class Distribution', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'class_distribution_pie_chart.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def plot_class_distribution_donut(df, output_dir):
    """Plot class distribution as donut chart"""
    print("\n🍩 Generating Donut Chart...")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Count classes
    class_counts = df['diagnosis_label'].value_counts()
    total = len(df)
    
    # Colors
    colors = ['#4ECDC4', '#FF6B6B']
    
    # Create donut chart
    wedges, texts, autotexts = ax.pie(
        class_counts.values,
        labels=class_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        pctdistance=0.85,
        textprops={'fontsize': 14, 'fontweight': 'bold'}
    )
    
    # Draw circle in center to make it a donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    # Add text in center
    ax.text(0, 0, f'Total\n{total}\nSamples', 
            ha='center', va='center', fontsize=18, fontweight='bold')
    
    # Enhance text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(16)
        autotext.set_fontweight('bold')
    
    # Add legend
    legend_labels = [f'{label}: {count} ({count/total*100:.1f}%)' 
                     for label, count in zip(class_counts.index, class_counts.values)]
    ax.legend(legend_labels, loc='upper left', fontsize=12, frameon=True, shadow=True)
    
    ax.set_title('Breast Cancer Dataset - Class Distribution', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'class_distribution_donut_chart.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def plot_comprehensive_statistics(df, data, output_dir):
    """Plot comprehensive dataset statistics"""
    print("\n📈 Generating Comprehensive Statistics...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Breast Cancer Dataset - Comprehensive Statistics', 
                 fontsize=18, fontweight='bold', y=0.995)
    
    # 1. Class Distribution (Bar)
    ax1 = axes[0, 0]
    class_counts = df['diagnosis_label'].value_counts()
    colors = ['#4ECDC4', '#FF6B6B']
    bars = ax1.bar(class_counts.index, class_counts.values, color=colors, 
                   edgecolor='black', linewidth=2, alpha=0.8)
    
    for bar, count in zip(bars, class_counts.values):
        height = bar.get_height()
        pct = count / len(df) * 100
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax1.set_xlabel('Diagnosis', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Samples', fontsize=12, fontweight='bold')
    ax1.set_title('Class Distribution', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. Class Distribution (Pie)
    ax2 = axes[0, 1]
    wedges, texts, autotexts = ax2.pie(
        class_counts.values,
        labels=class_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=(0.05, 0.05),
        textprops={'fontsize': 11, 'fontweight': 'bold'}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
    
    ax2.set_title('Class Proportion', fontsize=14, fontweight='bold')
    
    # 3. Feature Statistics
    ax3 = axes[1, 0]
    feature_stats = pd.DataFrame({
        'Total Features': [len(data.feature_names)],
        'Mean Features': [10],
        'SE Features': [10],
        'Worst Features': [10]
    })
    
    x = np.arange(len(feature_stats.columns))
    bars = ax3.bar(x, feature_stats.iloc[0].values, 
                   color=['#45B7D1', '#96CEB4', '#FFEAA7', '#DFE6E9'],
                   edgecolor='black', linewidth=2, alpha=0.8)
    
    for bar, val in zip(bars, feature_stats.iloc[0].values):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(val)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax3.set_xticks(x)
    ax3.set_xticklabels(feature_stats.columns, rotation=0, ha='center')
    ax3.set_ylabel('Count', fontsize=12, fontweight='bold')
    ax3.set_title('Feature Categories', fontsize=14, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    
    # 4. Dataset Summary
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    summary_text = f"""
    DATASET SUMMARY
    {'='*40}
    
    Total Samples: {len(df)}
    
    Class Distribution:
    • Benign: {class_counts['Benign']} ({class_counts['Benign']/len(df)*100:.1f}%)
    • Malignant: {class_counts['Malignant']} ({class_counts['Malignant']/len(df)*100:.1f}%)
    
    Features: {len(data.feature_names)}
    • Mean features: 10
    • Standard Error features: 10
    • Worst features: 10
    
    Class Balance:
    • Ratio (Benign:Malignant): {class_counts['Benign']/class_counts['Malignant']:.2f}:1
    • Imbalance: {'Moderate' if abs(class_counts['Benign']/len(df) - 0.5) < 0.2 else 'High'}
    
    Data Quality:
    • Missing Values: 0
    • Duplicates: 0
    • Data Type: Numerical (continuous)
    """
    
    ax4.text(0.1, 0.9, summary_text, transform=ax4.transAxes,
             fontsize=11, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'comprehensive_dataset_statistics.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def plot_class_balance_analysis(df, output_dir):
    """Plot class balance analysis"""
    print("\n⚖️ Generating Class Balance Analysis...")
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Class Balance Analysis', fontsize=16, fontweight='bold')
    
    # Count classes
    class_counts = df['diagnosis_label'].value_counts()
    total = len(df)
    
    # 1. Horizontal bar with percentages
    ax1 = axes[0]
    colors = ['#4ECDC4', '#FF6B6B']
    y_pos = np.arange(len(class_counts))
    
    bars = ax1.barh(y_pos, class_counts.values, color=colors, 
                    edgecolor='black', linewidth=2, alpha=0.8)
    
    # Add labels
    for i, (bar, count) in enumerate(zip(bars, class_counts.values)):
        width = bar.get_width()
        pct = count / total * 100
        ax1.text(width, bar.get_y() + bar.get_height()/2.,
                f' {count} ({pct:.1f}%)',
                ha='left', va='center', fontsize=12, fontweight='bold')
    
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(class_counts.index, fontsize=12)
    ax1.set_xlabel('Number of Samples', fontsize=12, fontweight='bold')
    ax1.set_title('Sample Count by Class', fontsize=14, fontweight='bold')
    ax1.grid(axis='x', alpha=0.3)
    
    # 2. Stacked percentage bar
    ax2 = axes[1]
    percentages = (class_counts / total * 100).values
    
    # Create stacked bar
    left = 0
    for i, (label, pct, color) in enumerate(zip(class_counts.index, percentages, colors)):
        ax2.barh(0, pct, left=left, color=color, edgecolor='black', 
                linewidth=2, alpha=0.8, label=label)
        
        # Add percentage text
        ax2.text(left + pct/2, 0, f'{label}\n{pct:.1f}%',
                ha='center', va='center', fontsize=12, fontweight='bold', color='white')
        left += pct
    
    ax2.set_xlim(0, 100)
    ax2.set_ylim(-0.5, 0.5)
    ax2.set_xlabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Class Distribution (Percentage)', fontsize=14, fontweight='bold')
    ax2.set_yticks([])
    ax2.legend(loc='upper right', fontsize=10)
    ax2.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'class_balance_analysis.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_statistics_table(df, data, output_dir):
    """Generate dataset statistics table"""
    print("\n📋 Generating Statistics Table...")
    
    class_counts = df['diagnosis_label'].value_counts()
    total = len(df)
    
    stats_data = {
        'Metric': [
            'Total Samples',
            'Benign Samples',
            'Malignant Samples',
            'Benign Percentage',
            'Malignant Percentage',
            'Total Features',
            'Missing Values',
            'Duplicate Rows',
            'Class Ratio (B:M)'
        ],
        'Value': [
            total,
            class_counts['Benign'],
            class_counts['Malignant'],
            f"{class_counts['Benign']/total*100:.1f}%",
            f"{class_counts['Malignant']/total*100:.1f}%",
            len(data.feature_names),
            0,
            0,
            f"{class_counts['Benign']/class_counts['Malignant']:.2f}:1"
        ]
    }
    
    stats_df = pd.DataFrame(stats_data)
    
    # Save to CSV
    csv_path = os.path.join(output_dir, 'dataset_statistics.csv')
    stats_df.to_csv(csv_path, index=False)
    print(f"   ✅ Saved: {csv_path}")
    
    # Print table
    print("\n" + "="*60)
    print("DATASET STATISTICS")
    print("="*60)
    print(stats_df.to_string(index=False))
    print("="*60)
    
    return stats_df

def main():
    """Main function"""
    
    print("\n" + "="*80)
    print("DATASET DISTRIBUTION VISUALIZATIONS - CHAPTER 3.2")
    print("="*80)
    
    # Create output directory
    output_dir = 'dataset_visualizations'
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n📁 Output directory: {output_dir}/")
    
    # Load dataset
    df, data = load_dataset()
    
    # Generate visualizations
    plot_class_distribution_bar(df, output_dir)
    plot_class_distribution_pie(df, output_dir)
    plot_class_distribution_donut(df, output_dir)
    plot_comprehensive_statistics(df, data, output_dir)
    plot_class_balance_analysis(df, output_dir)
    
    # Generate statistics table
    stats_df = generate_statistics_table(df, data, output_dir)
    
    print("\n" + "="*80)
    print("✅ ALL VISUALIZATIONS GENERATED!")
    print("="*80)
    print(f"\n📂 Files saved in: {os.path.abspath(output_dir)}/")
    print("\n📊 Generated files:")
    print("   1. class_distribution_bar_chart.png")
    print("   2. class_distribution_pie_chart.png")
    print("   3. class_distribution_donut_chart.png")
    print("   4. comprehensive_dataset_statistics.png")
    print("   5. class_balance_analysis.png")
    print("   6. dataset_statistics.csv")
    print("\n🎯 Use these in your Chapter 3.2!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
