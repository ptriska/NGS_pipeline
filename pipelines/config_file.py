reference_folder = "/mnt/storage/clip/Reference/"
output_folder = "/mnt/storage/clip/NGS_pipeline/RUN/"
input_folder = "/mnt/storage/clip/NGS_pipeline/TEST/input/"
bwa_index_GRCh38 = reference_folder+"/hg38_gatk/v0/"
bwa_index_hg19 = reference_folder+"/hg19_old_functional/broad_bundle_hg19_v2.5/"
reference_fasta_GRCh38 = reference_folder+"/hg38_gatk/v0/Homo_sapiens_assembly38.fasta"
reference_fasta_hg19 = reference_folder+"/hg19_old_functional/broad_bundle_hg19_v2.5/ucsc.hg19.fasta"
dbsnp_vcf_GRCh38 = reference_folder+"/GRCh38/hg38_broad_bundle/dbsnp_146.hg38.vcf.gz"
dbsnp_vcf_hg19 = reference_folder+"/hg19_old_functional/broad_bundle_hg19_v2.5/dbsnp_137.hg19.vcf"
vep_reference_folder_hg19 = reference_folder+"/hg19_old_functional/"
max_nr_threads= "20"
