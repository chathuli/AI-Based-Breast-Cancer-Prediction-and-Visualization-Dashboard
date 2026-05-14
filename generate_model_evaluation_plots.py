"""
Generate Confusion Matrix and ROC Curves for ML Models
Creates professional visualizations for model evaluation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    confusion_matrix, 
    classification_report, 
    roc_curve, 
    roc_auc_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
import os

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

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
    
    print(f"✅ Data loaded: {X_train.shape[0]} training, {X_test.shape[0]} test samples")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, data.target_names

def train_models(X_train, y_train):
    """Train all three models"""
    print("\n🤖 Training models...")
    
    models = {}
    
    print("   Training Logistic Regression...")
    lr = LogisticRegression(random_state=42, max_iter=10000)
    lr.fit(X_train, y_train)
    models['Logistic Regression'] = lr
    
    print("   Training Decision Tree...")
    dt = DecisionTreeClassifier(random_state=42, max_depth=5)
    dt.fit(X_train, y_train)
    models['Decision Tree'] = dt
    
    print("   Training SVM (Best Model)...")
    svm = SVC(kernel='rbf', random_state=42, probability=True)
    svm.fit(X_train, y_train)
    models['SVM'] = svm
    
    print("✅ All models trained!")
    
    return models

def plot_confusion_matrix(y_true, y_pred, model_name, target_names, save_path):
    """Plot confusion matrix"""
    
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(10, 8))
    
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues',
        xticklabels=target_names, yticklabels=target_names,
        cbar_kws={'label': 'Count'}, square=True,
        linewidths=1, linecolor='gray'
    )
    
    plt.title(f'Confusion Matrix - {model_name}', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('True Label', fontsize=12, fontweight='bold')
    plt.xlabel('Predicted Label', fontsize=12, fontweight='bold')
    
    accuracy = accuracy_score(y_true, y_pred)
    plt.text(
        0.5, -0.15, f'Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)',
        ha='center', transform=plt.gca().transAxes, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    )
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def plot_all_confusion_matrices(models, X_test, y_test, target_names, output_dir):
    """Plot confusion matrices for all models"""
    print("\n📊 Generating Confusion Matrices...")
    
    for model_name, model in models.items():
        y_pred = model.predict(X_test)
        save_path = os.path.join(output_dir, f'confusion_matrix_{model_name.replace(" ", "_").lower()}.png')
        plot_confusion_matrix(y_test, y_pred, model_name, target_names, save_path)

def plot_roc_curves(models, X_test, y_test, output_dir):
    """Plot ROC curves comparing all models"""
    print("\n📈 Generating ROC Curves...")
    
    plt.figure(figsize=(12, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    for idx, (model_name, model) in enumerate(models.items()):
        if hasattr(model, 'predict_proba'):
            y_pred_proba = model.predict_proba(X_test)[:, 1]
        else:
            y_pred_proba = model.decision_function(X_test)
        
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        auc_score = roc_auc_score(y_test, y_pred_proba)
        
        plt.plot(
            fpr, tpr, color=colors[idx], linewidth=2.5,
            label=f'{model_name} (AUC = {auc_score:.4f})',
            marker='o', markersize=4, markevery=20
        )
    
    plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier (AUC = 0.5000)')
    
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=12, fontweight='bold')
    plt.ylabel('True Positive Rate', fontsize=12, fontweight='bold')
    plt.title('ROC Curves - Model Comparison', fontsize=16, fontweight='bold', pad=20)
    plt.legend(loc='lower right', fontsize=11, frameon=True, shadow=True)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'roc_curves_comparison.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {save_path}")
    plt.close()

def generate_metrics_table(models, X_test, y_test, output_dir):
    """Generate metrics table"""
    print("\n📊 Generating Metrics Table...")
    
    metrics_data = []
    
    for model_name, model in models.items():
        y_pred = model.predict(X_test)
        
        if hasattr(model, 'predict_proba'):
            y_pred_proba = model.predict_proba(X_test)[:, 1]
        else:
            y_pred_proba = model.decision_function(X_test)
        
        metrics_data.append({
            'Model': model_name,
            'Accuracy': f'{accuracy_score(y_test, y_pred):.4f}',
            'Precision': f'{precision_score(y_test, y_pred):.4f}',
            'Recall': f'{recall_score(y_test, y_pred):.4f}',
            'F1-Score': f'{f1_score(y_test, y_pred):.4f}',
            'AUC': f'{roc_auc_score(y_test, y_pred_proba):.4f}'
        })
    
    metrics_df = pd.DataFrame(metrics_data)
    
    csv_path = os.path.join(output_dir, 'model_metrics_comparison.csv')
    metrics_df.to_csv(csv_path, index=False)
    print(f"   ✅ Saved: {csv_path}")
    
    print("\n" + "="*80)
    print("MODEL PERFORMANCE COMPARISON")
    print("="*80)
    print(metrics_df.to_string(index=False))
    print("="*80)
    
    return metrics_df

def main():
    """Main function"""
    
    print("\n" + "="*80)
    print("MODEL EVALUATION - CONFUSION MATRIX & ROC CURVES")
    print("="*80)
    
    output_dir = 'model_evaluation_results'
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n📁 Output directory: {output_dir}/")
    
    X_train, X_test, y_train, y_test, target_names = load_and_prepare_data()
    models = train_models(X_train, y_train)
    plot_all_confusion_matrices(models, X_test, y_test, target_names, output_dir)
    plot_roc_curves(models, X_test, y_test, output_dir)
    metrics_df = generate_metrics_table(models, X_test, y_test, output_dir)
    
    print("\n" + "="*80)
    print("✅ ALL EVALUATION PLOTS GENERATED!")
    print("="*80)
    print(f"\n📂 Files saved in: {os.path.abspath(output_dir)}/")
    print("\n📊 Generated files:")
    print("   1. confusion_matrix_logistic_regression.png")
    print("   2. confusion_matrix_decision_tree.png")
    print("   3. confusion_matrix_svm.png (Best Model)")
    print("   4. roc_curves_comparison.png")
    print("   5. model_metrics_comparison.csv")
    print("\n🎯 Use these in your Chapter 7!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
