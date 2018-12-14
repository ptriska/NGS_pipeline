import sys
import os
import subprocess


java_tempdir="/mnt/storage/clip/NGS_pipeline/java_temp"

def check_path(path):                		## Check if file exists
		if os.path.exists(path) == True:
			return True
		else:
			return False

def checkContainer(container_name):
		containers = subprocess.check_output(['docker','ps','-a']).decode(encoding="437")
		if container_name in containers.split():
			subprocess.call(["docker","rm",container_name])
		else:
			return	

def gatk_docker(tool, parameters_dict, log, ram, image, base_folder, reference_folder):
	container_name = (log.split("/")[-1]).replace(".log","")
	checkContainer(container_name)

		
	tools_dict	=		{
									"gatk_mark_duplicates":"MarkDuplicates",
									"gatk_add_read_groups":"AddOrReplaceReadGroups",
									"gatk_build_recalibrator":"BaseRecalibrator",	
									"gatk_apply_recalibrator":"ApplyBQSR",
									"gatk_haplotype_caller":"HaplotypeCaller",
									"gatk_mutect2":"Mutect2",
									"gatk_filter_mutect":"FilterMutectCalls"	
										}
				
	translate_parameters_dict = {
									"input":"-I",
									"input_normal":"-I",
									"input_tumor":"-I",
									"normal-sample":"-normal",
									"tumor-sample":"-tumor",
									"output":"-O",
									"mark_dupl_metrics":"-M",
									"optical_duplicate_pixel_dist":"--OPTICAL_DUPLICATE_PIXEL_DISTANCE",
									"assume_sort_order":"--ASSUME_SORT_ORDER",
									"clear_DT":"--CLEAR_DT",
									"add_pg_tag_to_reads":"--ADD_PG_TAG_TO_READS",
									"RGLB":"--RGLB",
									"RGPL":"--RGPL",
									"RGPU":"--RGPU",
									"RGSM":"--RGSM",
									"reference":"-R",
									"known-sites":"--known-sites",
									"use-original-qualities":"--use-original-qualities",
									"bqsr":"--bqsr",
									"static-quantized-quals":"--static-quantized-quals",
									"emit-reference-confidence":"--ERC",
									"max-alternate-alleles":"--max-alternate-alleles",
									"MODE":"--MODE",
									"variant":"-V"
										}
	cmd = [tools_dict[tool]]
	
	for key, value in parameters_dict.iteritems():
		if key in translate_parameters_dict:
			if value !="":
				cmd += [translate_parameters_dict[key], str(value)]
			else:
				cmd += [translate_parameters_dict[key]]	
		else:
			if value !="":
				cmd += [key, str(value)]	
			else:
				cmd += [key]
	
	
	""" Run a command inside docker container"""
	dcmd = ["docker", "run","--name",container_name,"-v", "{}:{}".format(base_folder, base_folder),"-v", "{}:{}".format(reference_folder, reference_folder), image]
	dcmd += ["gatk"]
	dcmd += ["--java-options" ,"-Djava.io.tmpdir="+java_tempdir]
	dcmd += cmd
	stderr = open(log,"w")
	print >> sys.stderr, "GATK: "," ".join(dcmd)
	#os.system(" ".join(dcmd))		
	errcode = subprocess.call(dcmd, stderr=stderr)
	checkContainer(container_name)
