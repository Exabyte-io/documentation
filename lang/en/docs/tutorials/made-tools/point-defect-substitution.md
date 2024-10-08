# Create materials with substitution defects from the paper 

This tutorial helps creating materials from Formation, stabilities, and electronic properties of nitrogen defects in graphene [1](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446) paper.

## Step 0: Open Materials Designer

## Step 1: Import Graphene material

In order to create a material with substitution defects in Graphene, the user should first import structure of Graphene into the current Materials Designer session, from the [Standata](../../materials-designer/header-menu/input-output/standata-import.md).

## Step 2: Use JupyterLite Session Dialog

Navigate to `Advanced` > `JupyterLite Session` from the main interface.

  <img src="/images/tutorials/interface_with_zsl/1_select_jupyterlite_session.webp" alt="Open JupyterLite Dialog"/>

- In the Introduction notebook find the link to the example under `Examples` > `1. Builders / Point Defects` > `1.1. Susbstitution defects in Graphene`

  <img src="/images/tutorials/interface_with_zsl/2_introduction_notebook.webp" alt="Open Example Notebook"/>
  
- The link will open the example notebook in a new tab.

## Step 3: Adjust notebook settings

- We need to create a 4x4 supercell of Graphene to introduce substitution defects. 
- We will focus on adding nitrogen atoms to the Graphene structure.
- Set the coordinate and element of the nitrogen atom to be added to the Graphene structure.


## Step 4: Run the Notebook

{% include 'includes/jupyterlite_embed.html' %}

## Step 5: Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

## Step 6: Save the Material

The user can save the material with substitution defects in the current Materials Designer session.

Or the user can download the material in Material JSON format or POSCAR format.

