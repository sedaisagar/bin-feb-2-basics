"""
Visualization examples using Matplotlib, Seaborn, and Plotly
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)


def plot_with_matplotlib():
    """Create a line plot with Matplotlib"""
    print("Creating Matplotlib visualization...")
    
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Create figure and plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)', linewidth=2, color='#1f77b4')
    plt.plot(x, y2, label='cos(x)', linewidth=2, color='#ff7f0e')
    
    plt.xlabel('X Axis', fontsize=12, fontweight='bold')
    plt.ylabel('Y Axis', fontsize=12, fontweight='bold')
    plt.title('Matplotlib: Trigonometric Functions', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('matplotlib_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Matplotlib plot saved as 'matplotlib_plot.png'")
    plt.show()


def plot_with_seaborn():
    """Create a statistical plot with Seaborn"""
    print("\nCreating Seaborn visualization...")
    
    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Category': np.repeat(['A', 'B', 'C', 'D'], 25),
        'Values': np.concatenate([
            np.random.normal(100, 15, 25),
            np.random.normal(110, 20, 25),
            np.random.normal(105, 18, 25),
            np.random.normal(95, 12, 25)
        ])
    })
    
    # Create figure
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data, x='Category', y='Values', palette='Set2')
    sns.stripplot(data=data, x='Category', y='Values', 
                  color='black', alpha=0.5, size=8)
    
    plt.xlabel('Category', fontsize=12, fontweight='bold')
    plt.ylabel('Values', fontsize=12, fontweight='bold')
    plt.title('Seaborn: Distribution Across Categories', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('seaborn_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Seaborn plot saved as 'seaborn_plot.png'")
    plt.show()


def plot_with_plotly():
    """Create an interactive plot with Plotly"""
    print("\nCreating Plotly visualization...")
    
    # Generate sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [65, 78, 84, 92, 88, 95, 102, 98, 87, 76, 81, 94]
    expenses = [40, 45, 50, 48, 52, 60, 65, 62, 55, 48, 50, 58]
    
    # Create figure
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(
        x=months, y=sales,
        mode='lines+markers',
        name='Sales',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=expenses,
        mode='lines+markers',
        name='Expenses',
        line=dict(color='#ff7f0e', width=3),
        marker=dict(size=10)
    ))
    
    # Update layout
    fig.update_layout(
        title='Plotly: Monthly Sales vs Expenses (Interactive)',
        xaxis_title='Month',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        template='plotly_white',
        width=1000,
        height=600,
        font=dict(size=12)
    )
    
    # Save and show
    fig.write_html('plotly_plot.html')
    print("✓ Plotly plot saved as 'plotly_plot.html'")
    fig.show()


def main():
    """Run all visualizations"""
    print("=" * 60)
    print("VISUALIZATION EXAMPLES")
    print("=" * 60)
    
    try:
        plot_with_matplotlib()
        plot_with_seaborn()
        plot_with_plotly()
        
        print("\n" + "=" * 60)
        print("All visualizations created successfully!")
        print("=" * 60)
        print("\nGenerated files:")
        print("  - matplotlib_plot.png")
        print("  - seaborn_plot.png")
        print("  - plotly_plot.html")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        print("Make sure you have installed: matplotlib, seaborn, plotly")


if __name__ == "__main__":
    main()
