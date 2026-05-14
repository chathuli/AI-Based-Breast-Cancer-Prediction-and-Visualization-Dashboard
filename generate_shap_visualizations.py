"""
Generate SHAP Visualization Examples for Chapters 6.4 and 7.4
Creates professional SHAP plots demonstrating explainable AI features
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import shap
import os
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

def load_and_prepare_data():
    """Load and prepare the breast cancer dataset"""
    print("📊 Loading breast cancer dataset...")
    
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='target')
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Convert back to DataFrame for feature names
    X_train_df = pd.DataFrame(X_train_scaled, columns=data.feature_names)
    X_test_df = pd.DataFrame(X_test_scaled, columns=data.feature_names)
    
    print(f"✅ Data loaded: {X_train.shape[0]} training, {X_test.shape[0]} test samples")
    
    return X_train_df, X_test_df, y_train, y_test, data

def train_model(X_train, y_train):
    """Train SVM model"""
    print("\n🤖 Training SVM model...")
    
    model = SVC(kernel='rbf', random_state=42, probability=True)
    model.fit(X_train, y_train)
    
    print("✅ Model trained successfully!")
    
    return model

def create_shap_explainer(model, X_train):
    """Create SHAP explainer"""
    print("\n🔍 Creating SHAP explainer...")
    
    # Use KernelExplainer for SVM
    explainer = shap.KernelExplainer(model.predict_proba, shap.sample(X_train, 100))
    
    print("✅ SHAP explainer created!")
    
    return explainer

def generate_force_plot(explainer, X_test, model, output_dir, sample_idx=0):
    """Generate SHAP force plot"""
    print(f"\n📊 Generating force plot for sample {sample_idx}...")
    
    # Get SHAP values for one sample
    shap_values = explainer.shap_values(X_test.iloc[sample_idx:sample_idx+1])
    
    # Get prediction
    prediction = model.predict(X_test.iloc[sample_idx:sample_idx+1])[0]
    pred_proba = model.predict_proba(X_test.iloc[sample_idx:sample_idx+1])[0]
    
    # Create force plot
    shap.force_plot(
        explainer.expected_value[1],
        shap_values[1][0],
        X_test.iloc[sample_idx],
        matplotlib=True,
        show=False
    )
    
    plt.title(f'SHAP Force Plot - Sample {sample_idx}\n'
              f'Prediction: {"Benign" if prediction == 1 else "Malignant"} '
              f'(Probability: {pred_proba[prediction]:.3f})',
              fontsize=12, fontweight='bold', pad=20)
    
    save_path = os.path.join(output_dir, f'shap_force_plot_sample_{sample_idx}.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_waterfall_plot(explainer, X_test, model, output_dir, sample_idx=0):
    """Generate SHAP waterfall plot"""
    print(f"\n💧 Generating waterfall plot for sample {sample_idx}...")
    
    # Get SHAP values
    shap_values = explainer.shap_values(X_test.iloc[sample_idx:sample_idx+1])
    
    # Get prediction
    prediction = model.predict(X_test.iloc[sample_idx:sample_idx+1])[0]
    pred_proba = model.predict_proba(X_test.iloc[sample_idx:sample_idx+1])[0]
    
    # Create explanation object
    explanation = shap.Explanation(
        values=shap_values[1][0],
        base_values=explainer.expected_value[1],
        data=X_test.iloc[sample_idx].values,
        feature_names=X_test.columns.tolist()
    )
    
    # Create waterfall plot
    plt.figure(figsize=(10, 8))
    shap.waterfall_plot(explanation, show=False)
    
    plt.title(f'SHAP Waterfall Plot - Sample {sample_idx}\n'
              f'Prediction: {"Benign" if prediction == 1 else "Malignant"} '
              f'(Probability: {pred_proba[prediction]:.3f})',
              fontsize=12, fontweight='bold', pad=20)
    
    save_path = os.path.join(output_dir, f'shap_waterfall_plot_sample_{sample_idx}.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_summary_plot(explainer, X_test, output_dir):
    """Generate SHAP summary plot"""
    print("\n📊 Generating summary plot...")
    
    # Calculate SHAP values for test set (sample for speed)
    X_test_sample = X_test.sample(min(50, len(X_test)), random_state=42)
    shap_values = explainer.shap_values(X_test_sample)
    
    # Handle different SHAP value formats
    if isinstance(shap_values, list):
        shap_vals = shap_values[1]  # For binary classification, use positive class
    else:
        shap_vals = shap_values
    
    # Create summary plot
    plt.figure(figsize=(12, 8))
    shap.summary_plot(shap_vals, X_test_sample.values, 
                     feature_names=X_test_sample.columns.tolist(), show=False)
    plt.title('SHAP Summary Plot - Feature Importance', 
              fontsize=14, fontweight='bold', pad=20)
    
    save_path = os.path.join(output_dir, 'shap_summary_plot.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_bar_plot(explainer, X_test, output_dir):
    """Generate SHAP bar plot"""
    print("\n📊 Generating bar plot...")
    
    # Calculate SHAP values
    X_test_sample = X_test.sample(min(50, len(X_test)), random_state=42)
    shap_values = explainer.shap_values(X_test_sample)
    
    # Handle different SHAP value formats
    if isinstance(shap_values, list):
        shap_vals = shap_values[1]
    else:
        shap_vals = shap_values
    
    # Create bar plot
    plt.figure(figsize=(10, 8))
    shap.summary_plot(shap_vals, X_test_sample.values,
                     feature_names=X_test_sample.columns.tolist(),
                     plot_type="bar", show=False)
    plt.title('SHAP Bar Plot - Mean Feature Importance', 
              fontsize=14, fontweight='bold', pad=20)
    
    save_path = os.path.join(output_dir, 'shap_bar_plot.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_decision_plot(explainer, X_test, model, output_dir):
    """Generate SHAP decision plot"""
    print("\n📊 Generating decision plot...")
    
    # Calculate SHAP values for a few samples
    X_test_sample = X_test.sample(min(20, len(X_test)), random_state=42)
    shap_values = explainer.shap_values(X_test_sample)
    
    # Handle different SHAP value formats
    if isinstance(shap_values, list):
        shap_vals = shap_values[1]
    else:
        shap_vals = shap_values
    
    # Create decision plot
    plt.figure(figsize=(10, 8))
    shap.decision_plot(
        explainer.expected_value[1] if isinstance(explainer.expected_value, list) else explainer.expected_value,
        shap_vals,
        X_test_sample.values,
        feature_names=X_test_sample.columns.tolist(),
        show=False
    )
    plt.title('SHAP Decision Plot - Prediction Paths', 
              fontsize=14, fontweight='bold', pad=20)
    
    save_path = os.path.join(output_dir, 'shap_decision_plot.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_multiple_samples(explainer, X_test, model, output_dir):
    """Generate force and waterfall plots for multiple samples"""
    print("\n📊 Generating plots for multiple samples...")
    
    # Select diverse samples (benign and malignant predictions)
    predictions = model.predict(X_test)
    
    # Get indices for benign and malignant predictions
    benign_indices = np.where(predictions == 1)[0][:2]
    malignant_indices = np.where(predictions == 0)[0][:2]
    
    sample_indices = list(benign_indices) + list(malignant_indices)
    
    for idx in sample_indices:
        try:
            generate_force_plot(explainer, X_test, model, output_dir, idx)
            generate_waterfall_plot(explainer, X_test, model, output_dir, idx)
        except Exception as e:
            print(f"   ⚠️ Error generating plots for sample {idx}: {e}")

def create_comparison_plot(explainer, X_test, model, output_dir):
    """Create side-by-side comparison of benign and malignant predictions"""
    print("\n📊 Creating comparison plot...")
    
    predictions = model.predict(X_test)
    
    # Get one benign and one malignant sample
    benign_idx = np.where(predictions == 1)[0][0]
    malignant_idx = np.where(predictions == 0)[0][0]
    
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    fig.suptitle('SHAP Explanation Comparison: Benign vs Malignant', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    for idx, (sample_idx, label) in enumerate([(benign_idx, 'Benign'), 
                                                 (malignant_idx, 'Malignant')]):
        shap_values = explainer.shap_values(X_test.iloc[sample_idx:sample_idx+1])
        pred_proba = model.predict_proba(X_test.iloc[sample_idx:sample_idx+1])[0]
        
        # Handle different SHAP value formats
        if isinstance(shap_values, list):
            shap_vals = shap_values[1][0]
        else:
            shap_vals = shap_values[0]
        
        # Ensure shap_vals is 1D
        if len(shap_vals.shape) > 1:
            shap_vals = shap_vals.flatten()
        
        # Get top features
        feature_importance = pd.DataFrame({
            'feature': X_test.columns.tolist(),
            'shap_value': shap_vals.tolist()
        }).sort_values('shap_value', key=abs, ascending=False).head(10)
        
        ax = axes[idx]
        colors = ['red' if x < 0 else 'green' for x in feature_importance['shap_value']]
        ax.barh(range(len(feature_importance)), feature_importance['shap_value'], color=colors)
        ax.set_yticks(range(len(feature_importance)))
        ax.set_yticklabels(feature_importance['feature'], fontsize=9)
        ax.set_xlabel('SHAP Value', fontweight='bold')
        ax.set_title(f'{label} Prediction\n(Probability: {pred_proba[1 if label=="Benign" else 0]:.3f})',
                    fontweight='bold')
        ax.axvline(x=0, color='black', linestyle='--', linewidth=1)
        ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'shap_comparison_benign_vs_malignant.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_feature_dependence_plots(explainer, X_test, output_dir):
    """Generate SHAP dependence plots for top features"""
    print("\n📊 Generating dependence plots...")
    
    # Calculate SHAP values
    X_test_sample = X_test.sample(min(50, len(X_test)), random_state=42)
    shap_values = explainer.shap_values(X_test_sample)
    
    # Handle different SHAP value formats
    if isinstance(shap_values, list):
        shap_vals = shap_values[1]
    else:
        shap_vals = shap_values
    
    # Get top 4 features
    mean_abs_shap = np.abs(shap_vals).mean(axis=0)
    top_features_idx = np.argsort(mean_abs_shap)[-4:]
    top_features = X_test.columns[top_features_idx]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('SHAP Dependence Plots - Top Features', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    for idx, (ax, feature) in enumerate(zip(axes.flat, top_features)):
        shap.dependence_plot(
            feature,
            shap_vals,
            X_test_sample.values,
            feature_names=X_test_sample.columns.tolist(),
            ax=ax,
            show=False
        )
        ax.set_title(f'{feature}', fontweight='bold')
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'shap_dependence_plots.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def main():
    """Main function"""
    
    print("\n" + "="*80)
    print("SHAP VISUALIZATION GENERATION - CHAPTERS 6.4 & 7.4")
    print("="*80)
    
    # Create output directory
    output_dir = 'shap_visualizations'
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n📁 Output directory: {output_dir}/")
    
    # Load data and train model
    X_train, X_test, y_train, y_test, data = load_and_prepare_data()
    model = train_model(X_train, y_train)
    
    # Create SHAP explainer
    explainer = create_shap_explainer(model, X_train)
    
    # Generate visualizations
    print("\n" + "="*80)
    print("GENERATING SHAP VISUALIZATIONS")
    print("="*80)
    
    # Generate multiple sample plots
    generate_multiple_samples(explainer, X_test, model, output_dir)
    
    # Generate summary plots
    generate_summary_plot(explainer, X_test, output_dir)
    generate_bar_plot(explainer, X_test, output_dir)
    
    # Generate comparison plot
    create_comparison_plot(explainer, X_test, model, output_dir)
    
    # Generate decision plot
    try:
        generate_decision_plot(explainer, X_test, model, output_dir)
    except Exception as e:
        print(f"   ⚠️ Could not generate decision plot: {e}")
    
    # Generate dependence plots
    try:
        generate_feature_dependence_plots(explainer, X_test, output_dir)
    except Exception as e:
        print(f"   ⚠️ Could not generate dependence plots: {e}")
    
    print("\n" + "="*80)
    print("✅ ALL SHAP VISUALIZATIONS GENERATED!")
    print("="*80)
    print(f"\n📂 Files saved in: {os.path.abspath(output_dir)}/")
    print("\n📊 Generated visualizations:")
    print("   • Force plots (multiple samples)")
    print("   • Waterfall plots (multiple samples)")
    print("   • Summary plot (feature importance)")
    print("   • Bar plot (mean importance)")
    print("   • Comparison plot (benign vs malignant)")
    print("   • Decision plot (prediction paths)")
    print("   • Dependence plots (feature interactions)")
    print("\n🎯 Use these in Chapters 6.4 and 7.4!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
