import scvi
import scanpy as sc

# adata_combined = sc.read_h5ad("../data/2ndRun/adata_combined.h5ad")
adata_combined = sc.read_h5ad("../data/2ndRun/adata_combined_broad.h5ad")
# adata_combined = sc.read_h5ad("../data/2ndRun/adata_combined_group.h5ad")
# adata_combined = sc.read_h5ad("../data/2ndRun/adata_combined_nastia.h5ad")
# adata_combined = sc.read_h5ad("../data/2ndRun/adata_combined_gut.h5ad")

scvi.model.SCANVI.setup_anndata(
    adata_combined,
    layer=None,  #use the normalized data in X
    # labels_key='adfca_annotation', 
    labels_key='adfca_annotation_broad',
    # labels_key='adfca_annotation_group',
    # labels_key='fine_annot_v4_predicted', 
    unlabeled_category='Unknown',   
    batch_key='batch'        
)

#Initialize the model
model = scvi.model.SCANVI(adata_combined, n_latent=30, n_hidden=128, n_layers=2)

#Train the model
model.train(max_epochs=1000, early_stopping=True, early_stopping_patience=20) 

# Save the model
# model.save("../data/2ndRun/scanvi_trained_model", overwrite=True)
model.save("../data/2ndRun/broad_trained_model", overwrite=True)
# model.save("../data/2ndRun/group_trained_model", overwrite=True)
# model.save("../data/2ndRun/nastia_trained_model", overwrite=True)
# model.save("../data/2ndRun/gut_trained_model", overwrite=True)
