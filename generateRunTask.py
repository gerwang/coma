template = 'cd /home/jingwang/Data/git-task/coma ' \
           '&& /home/jingwang/Data/anaconda3/envs/coma/bin/python ' \
           '%s.py --data data/%s --name %s --template data/fw_template.obj' \
           ' --nz %d' \
           ' > results/logs/%s.log 2>&1'

mains = ['main', 'main_v2', 'main_v3', 'main_v4']
datasets = ['FW_140', 'FW_500', 'FW_2000', 'FW_10000']
nzs = [8]
with open('tasks.txt', 'w') as f:
    for nz in nzs:
        for main in mains:
            for dataset in datasets:
                name = '%s_%s_%d' % (main, dataset, nz)
                task = template % (main, dataset, name, nz, name)
                print(task)
                f.write(task + '\n')
