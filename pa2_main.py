from function.tsp_simulated_annealing import tsp
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--o', '--output_root', help='path to the output files', default='./tsp_results')
    parser.add_argument('--n', '--num_points', default=20, help='number of points')
    parser.add_argument('--i', '--iterations', default=10000, help='number of iterations')
    parser.add_argument('--t', '--temperature', default=500000, help='initial temperature')
    parser.add_argument('--w', '--width', default=1000, help='width of the field')
    parser.add_argument('--f', '--file', default='./tsp_results/tsp_20.txt', help='path to point file')
    opt = parser.parse_args()

    result_dist_list = []
    for i in range(20):
        tsp_problem = tsp(num_points=opt.n, width=opt.w, point_file=opt.f, n_iterations=opt.i)
        tsp_problem.simulated_annealing(temperature=opt.t)
        print(f'Done! best distance = {tsp_problem.best_distance[-1][0]}')
        result_dist_list.append(tsp_problem.best_distance[-1][0])
        tsp_problem.save_best_result(filename=os.path.join(opt.o, f'tsp_{opt.n}_{tsp_problem.best_distance[-1][0]}_path.txt'))
        tsp_problem.plot_path(best=True, save_name=os.path.join(opt.o, f'tsp_{opt.n}_{tsp_problem.best_distance[-1][0]}_path.png'))
        tsp_problem.plot_dis_decay(save_name=os.path.join(opt.o, f'tsp_{opt.n}_{tsp_problem.best_distance[-1][0]}_curve.png'))
    print(sorted(result_dist_list, key = lambda x:float(x)))
    print(len(result_dist_list))