# BDF
 Pour le lancer sur le finisTerrae III, normalement en 11 minutes c'est fini. Il faut peut être changer les lignes pour activer python.
srun --time=00:59:00 --mem=16G -c 32 --pty bash
source /mnt/lustre/scratch/nlsas/home/ulc/cursos/curso341/miniconda3/bin/activate # ACTIVER PYTHON
conda activate DaskOnRay38 # ACTIVER PYTHON
jupyter lab --ip `hostname -i`

Ensuite sur le notebook:
- Copier le premier lien
- Appuyer sur select kernel -> Existing Jupyter Server
- Coller le lien
- Selectionner mypython
- Lancer le notebook
