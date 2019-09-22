import math

template = 'cd /home/jingwang/Data/git-task/coma ' \
           '&& /home/jingwang/Data/anaconda3/envs/coma/bin/python ' \
           '%s.py --data data/%s --name %s --template data/fw_template.obj' \
           ' --nz %d --num_epochs %d' \
           ' > results/logs/%s.log 2>&1'

mains = ['main', 'main_v2', 'main_v3', 'main_v4']
datasets = ['FW_all_500', 'FW_all_2000', 'FW_all_10000', 'FW_front_500', 'FW_front_2000']
nzs = [8]


def get_num_epoches(name):
    coma_num = 20466
    coma_epoch = 300
    my_num = int(name.split('_')[-2])
    my_epoch = int(math.ceil(float(coma_num * coma_epoch) / my_num))
    return my_epoch


with open('tasks.txt', 'w') as f:
    for nz in nzs:
        for main in mains:
            for dataset in datasets:
                name = '%s_%s_%d' % (main, dataset, nz)
                task = template % (main, dataset, name, nz, get_num_epoches(name), name)
                print(task)
                f.write(task + '\n')
