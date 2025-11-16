# Neural Network Interpretability for Prisoner's Dilemma

A research project investigating how evolved artificial neural networks encode strategic concepts in game-theoretic interactions, with a focus on cooperation, retaliation, and forgiveness in the Prisoner's Dilemma. We evolve neural networks to play the Prisoner's Dilemma, then use mechanistic interpretability techniques to decode what strategic concepts each neuron represents.

## Quick Start

```bash
# Environment setup
source venv/bin/activate
export OPENAI_API_KEY="your-api-key"

# Core analysis pipeline
./scripts/record_neurons.sh    # Record neuron activations against strategies
./scripts/gen_prompts.sh       # Generate GPT-4 interpretation prompts  
./scripts/gen_explanations.sh  # Obtain neuron-level interpretations
```

## Methodology

1. **Evolution**: Train artificial neural networks using the Axelrod library to compete in Prisoner's Dilemma tournaments
2. **Recording**: Capture neuron activations during gameplay against canonical strategies (Tit-for-Tat, Always Cooperate, etc.)
3. **Analysis**: Apply weighted activation aggregation to identify feature-neuron correlations
4. **Interpretation**: Use GPT-4 to generate human-readable explanations of neuron behavior patterns

## Repository Structure

```
├── ann_recorder.py           # Core recording module for neuron activations
├── generate_gpt_prompt.py    # Converts activation data to structured prompts
├── query.py                  # GPT-4 interface for neuron interpretations
├── utils.py                  # Visualization and analysis utilities
├── data/                     # Neural network parameters and activation data
│   ├── ann_*_params.csv     # Evolved network parameters (5-200 neurons)
│   ├── wa-*.pkl             # Weighted activation arrays
│   └── prompt-*.json        # Generated interpretation prompts
├── results/                  # GPT-4 explanations and analysis outputs
├── visuals/                  # Correlation heatmaps and visualizations
└── scripts/                  # Automated workflow scripts
```

## Usage Examples

### Single Network Analysis
```bash
# Record activations for 10-neuron network vs Tit-for-Tat
python3 ann_recorder.py data/ann_10_params.csv Tit_For_Tat

# Generate interpretation prompt
python3 generate_gpt_prompt.py data/prompt_header.txt data/wa-10-Tit_For_Tat.pkl data/prompt-10-Tit_For_Tat.json

# Obtain GPT-4 explanations
python3 query.py gpt-4 data/prompt-10-Tit_For_Tat.json results/explained-10-Tit_For_Tat.json
```

## Feature Engineering

The system tracks 17 behavioral features during gameplay:
- Opponent's first and second moves
- Historical cooperation/defection counts
- Round number and temporal patterns  
- Move sequences and strategic transitions
- Boolean indicators (0-1) and continuous measures

Weighted activation analysis reveals which neurons preferentially fire in response to specific strategic contexts, enabling interpretation of their computational role.