subjects=("airliner" "arctic-fox" "bee" "coco" "golden_retriever" "gorilla" "magnetic_compass" "peacock" "pelican" "snail" "zebra")

echo "${subjects[@]}"

for subject in "${subjects[@]}"; do
	echo $subject
	curl -LO https://raw.githubusercontent.com/openvinotoolkit/model_server/main/demos/common/static/images/$subject.jpeg
done
