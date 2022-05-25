MODEL1=/mnt/Storage/Result/unsupMASS_dumped/pre_deen/mass_ende_1024.pth
MODEL2=dumped/tc12_mass_deen_img_rl/fullreload1/best-valid_de-en_mt_bleu.pth
python train.py \
--exp_name \
tc12_mass_deen_img_rl \
--exp_id \
fullreload1 \
--data_path \
./data/processed/de-en/ \
--lgs \
"de-en" \
--mass_steps \
"de,en" \
--encoder_only \
false \
--emb_dim \
1024 \
--n_layers \
4 \
--n_heads \
8 \
--batch_size \
2 \
--dropout \
0.1 \
--attention_dropout \
0.1 \
--gelu_activation \
true \
--optimizer \
adam_inverse_sqrt,beta1=0.9,beta2=0.98,lr=0.00001 \
--epoch_size \
9000 \
--max_epoch \
20 \
--eval_bleu \
true \
--word_mass \
0.5 \
--min_len \
5 \
--beam_size \
2 \
--knowledge \
double_attn \
--k_emb_path \
./WN18RR/ent_embedding \
--use_image \
true \
--img_feature_file \
/mnt/Storage/Dataset/iaprtc12/iaprtc12-res4frelu.npy \
--fp16 \
true \
--reload_model \
"$MODEL1,$MODEL1" \
&& \
python train.py \
--exp_name \
tc12_bt_deen_img_rl \
--exp_id \
fullreload2 \
--data_path \
./data/processed/de-en/ \
--lgs \
de-en \
--bt_steps \
en-de-en,de-en-de \
--encoder_only \
false \
--emb_dim \
1024 \
--n_layers \
4 \
--n_heads \
8 \
--dropout \
0.1 \
--attention_dropout \
0.1 \
--gelu_activation \
true \
--batch_size \
8 \
--optimizer \
adam_inverse_sqrt,beta1=0.9,beta2=0.98,lr=0.0001 \
--epoch_size \
9000 \
--max_epoch \
10 \
--eval_bleu \
true \
--reload_model \
"$MODEL2,$MODEL2" \
--fp16 \
true \
--beam_size \
2
