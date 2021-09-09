# AUTOGENERATED! DO NOT EDIT! File to edit: 01_plots.ipynb (unless otherwise specified).

__all__ = ['DEFAULT_PARAMS', 'l_required_keys_ind_samples', 'l_required_keys_one_sample', 'l_required_keys_mma',
           'plot_independent_samples', 'initialize_plot', 'finish_show_and_save_plot',
           'annotate_stats_independent_samples', 'get_stars_str', 'plot_one_sample', 'annotate_stats_one_sample',
           'plot_mma', 'annotate_stats_mma', 'annotate_stats_mma_pointplot', 'sort_by_third']

# Cell
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Cell

DEFAULT_PARAMS = {'set_fig_width': 20,
                  'set_fig_height': 20,
                  'set_axes_linewidth': 1.5,
                  'set_axes_color': 'black',
                  'set_axes_tick_size': 15,
                  'set_yaxis_label_text': 'data',
                  'set_yaxis_label_fontsize': 15,
                  'set_yaxis_label_color': 'black',
                  'set_xaxis_label_text': 'groups',
                  'set_xaxis_label_fontsize': 15,
                  'set_xaxis_label_color': 'black',
                  'set_yaxis_scaling_mode': 1,
                  'set_yaxis_lower_lim_value': 0.3,
                  'set_yaxis_upper_lim_value': 0.9,
                  'distance_brackets_to_data': 0.05,
                  'annotation_brackets_factor': 1,
                  'distance_stars_to_brackets': 0.05,
                  'linewidth_annotations': 1.5,
                  'fontsize_stars': 15,
                  'fontweight_stars': 'bold',
                  'set_show_legend': True
                 }

l_required_keys_ind_samples = list(DEFAULT_PARAMS.keys())
l_required_keys_one_sample = list(DEFAULT_PARAMS.keys())
l_required_keys_mma = list(DEFAULT_PARAMS.keys())

# Cell
def plot_independent_samples(df, plot_type = 'stripplot', params = DEFAULT_PARAMS):
    "Handles all the plotting that is currently available for the comparison of two or more independent samples."
    if type(params) != dict:
        raise TypeError('params must be a dictionary')

    if 'data_col' not in list(params.keys()):
        params['data_col'] = df.columns[0]
        params['group_col'] = df.columns[1]
        #params['l_x_order'] = list(df[params['group_col']].unique())

    for elem in l_required_keys_ind_samples:
        if elem not in list(params.keys()):
            params[elem] = DEFAULT_PARAMS[elem]

    if plot_type in ['stripplot', 'boxplot', 'boxplot with stripplot overlay', 'violinplot', 'violinplot with stripplot overlay']:

        fig, ax = initialize_plot(params)

        if plot_type == 'stripplot':
            sns.stripplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          palette = params['color_palette'], size = params['set_marker_size'], ax=ax)
        elif plot_type == 'boxplot':
            sns.boxplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                        palette = params['color_palette'], ax=ax)
        elif plot_type == 'boxplot with stripplot overlay':
            sns.boxplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                        palette = params['color_palette'], ax=ax, showfliers=False)
            sns.stripplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          color = 'k', size = params['set_marker_size'], ax=ax)
        elif plot_type == 'violinplot':
            sns.violinplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                           palette = params['color_palette'], cut=0, ax=ax)
        elif plot_type == 'violinplot with stripplot overlay':
            sns.violinplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                           palette = params['color_palette'], cut=0, ax=ax)
            sns.stripplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          color = 'k', size = params['set_marker_size'], ax=ax)

        ax = annotate_stats_independent_samples(ax, df, params)

        finish_show_and_save_plot(ax, params)

    else: # if plot_type not in list of supported options
        if type(plot_type) != str:
            raise TypeError('plot_type must be of type string and one of the following options:\n \
                            ["stripplot", "boxplot", "boxplot with stripplot overlay", "violinplot", "violinplot with stripplot overlay"]')
        else:
            raise ValueError('plot_type must be one of the following options:\n \
                             ["stripplot", "boxplot", "boxplot with stripplot overlay", "violinplot", "violinplot with stripplot overlay"]')




# Cell
def initialize_plot(params):

    fig = plt.figure(figsize=(params['set_fig_width']/2.54 , params['set_fig_height']/2.54), facecolor='white')
    ax = fig.add_subplot()

    for axis in ['top', 'right']:
        ax.spines[axis].set_visible(False)

    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(params['set_axes_linewidth'])
        ax.spines[axis].set_color(params['set_axes_color'])

    ax.tick_params(labelsize=params['set_axes_tick_size'], colors=params['set_axes_color'])

    return fig, ax



# Cell
def finish_show_and_save_plot(ax, params):
    ax.set_ylabel(params['set_yaxis_label_text'], fontsize=params['set_yaxis_label_fontsize'], color=params['set_yaxis_label_color'])
    ax.set_xlabel(params['set_xaxis_label_text'], fontsize=params['set_xaxis_label_fontsize'], color=params['set_xaxis_label_color'])

    if params['set_yaxis_scaling_mode'] in [1, 'manual']: #1 for GUI, manual for API
        ax.set_ylim(params['set_yaxis_lower_lim_value'], params['set_yaxis_upper_lim_value'])

    plt.tight_layout()

    if params['save_plot'] == True:
        plt.savefig('customized_plot.png', dpi=300)

    plt.show()

# Cell
def annotate_stats_independent_samples(ax, df, params):
    l_stats_to_annotate = params['l_stats_to_annotate']
    if len(l_stats_to_annotate) > 0:

        max_total = df[params['data_col']].max()
        y_shift_annotation_line = max_total * params['distance_brackets_to_data']
        brackets_height = y_shift_annotation_line*0.5*params['annotation_brackets_factor']
        y_shift_annotation_text = brackets_height + y_shift_annotation_line*0.5*params['distance_stars_to_brackets']

        # Set initial y
        y = max_total + y_shift_annotation_line

        # Add check whether group level ANOVA / Kruska-Wallis-ANOVA is significant
        df_temp = params['results']['summary']['pairwise_comparisons'].copy()

        for group1, group2 in l_stats_to_annotate:

            x1 = params['l_xlabel_order'].index(group1)
            x2 = params['l_xlabel_order'].index(group2)

            stars = get_stars_str(df_temp, group1, group2, params)

            ax.plot([x1, x1, x2, x2], [y, y+brackets_height, y+brackets_height, y], c='k', lw=params['linewidth_annotations'])
            ax.text((x1+x2)*.5, y+y_shift_annotation_text, stars, ha='center', va='bottom', color='k',
                     fontsize=params['fontsize_stars'], fontweight=params['fontweight_stars'])

            # With set_distance_stars_to_brackets being limited to 5, stars will always be closer than next annotation line
            y = y+3*y_shift_annotation_line
    return ax

# Cell
def get_stars_str(df_tmp, group1, group2, params):
    if df_tmp.loc[(df_tmp['A'] == group1) & (df_tmp['B'] == group2)].shape[0] > 0:
        if 'p-corr' in df_tmp.loc[(df_tmp['A'] == group1) & (df_tmp['B'] == group2)].columns:
            pval = df_tmp.loc[(df_tmp['A'] == group1) & (df_tmp['B'] == group2), 'p-corr'].iloc[0]
        else:
            pval = df_tmp.loc[(df_tmp['A'] == group1) & (df_tmp['B'] == group2), 'p-unc'].iloc[0]

    elif df_tmp.loc[(df_tmp['B'] == group1) & (df_tmp['A'] == group2)].shape[0] > 0:
        if 'p-corr' in df_tmp.loc[(df_tmp['B'] == group1) & (df_tmp['A'] == group2)].columns:
            pval = df_tmp.loc[(df_tmp['B'] == group1) & (df_tmp['A'] == group2), 'p-corr'].iloc[0]
        else:
            pval = df_tmp.loc[(df_tmp['B'] == group1) & (df_tmp['A'] == group2), 'p-unc'].iloc[0]
    else:
        print('There was an error with annotating the stats!')
    if pval <= 0.001:
        stars = '***'
    elif pval <= 0.01:
        stars = '**'
    elif pval <= 0.05:
        stars = '*'
    else:
        stars = 'n.s.'

    return stars

# Cell
def plot_one_sample(df, plot_type = 'stripplot', params = DEFAULT_PARAMS):
    "Handles all the plotting that is currently available for the comparison of one group to a fixed value."
    if type(params) != dict:
        raise TypeError('params must be a dictionary')

    if 'data_col' not in list(params.keys()):
        params['data_col'] = df.columns[0]
        params['group_col'] = df.columns[1]
        params['fixed_value'] = df.columns[2]
        #params['l_x_order'] = list(df[params['group_col']].unique())

    for elem in l_required_keys_one_sample:
        if elem not in list(params.keys()):
            params[elem] = DEFAULT_PARAMS[elem]

    if plot_type in ['stripplot', 'boxplot', 'boxplot with stripplot overlay', 'violinplot', 'violinplot with stripplot overlay', 'histogram']:

        fig, ax = initialize_plot(params)

        if plot_type == 'stripplot':
            sns.stripplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          palette = params['color_palette'], size = params['set_marker_size'], ax=ax)
            ax.hlines(y = params['fixed_value'], xmin = -0.5, xmax = 0.5, color = 'gray', linestyle = 'dashed')
        elif plot_type == 'boxplot':
            sns.boxplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                        palette = params['color_palette'], ax=ax)
            ax.hlines(y = params['fixed_value'], xmin = -0.5, xmax = 0.5, color = 'gray', linestyle = 'dashed')
        elif plot_type == 'boxplot with stripplot overlay':
            sns.boxplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                        palette = params['color_palette'], ax=ax, showfliers=False)
            sns.stripplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          color = 'k', size = params['set_marker_size'], ax=ax)
            ax.hlines(y = params['fixed_value'], xmin = -0.5, xmax = 0.5, color = 'gray', linestyle = 'dashed')
        elif plot_type == 'violinplot':
            sns.violinplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                           palette = params['color_palette'], cut=0, ax=ax)
            ax.hlines(y = params['fixed_value'], xmin = -0.5, xmax = 0.5, color = 'gray', linestyle = 'dashed')
        elif plot_type == 'violinplot with stripplot overlay':
            sns.violinplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                           palette = params['color_palette'], cut=0, ax=ax)
            sns.stripplot(data = df, x = params['group_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          color = 'k', size = params['set_marker_size'], ax=ax)
            ax.hlines(y = params['fixed_value'], xmin = -0.5, xmax = 0.5, color = 'gray', linestyle = 'dashed')
        elif plot_type == 'histogram':
            print('This function (plot one sample data as histogram) is not yet implemented.')

        if plot_type in ['stripplot', 'boxplot', 'boxplot with stripplot overlay', 'violinplot', 'violinplot with stripplot overlay']:
            ax = annotate_stats_one_sample(ax, df, params)
        elif plot_type == 'histogram':
            print('This function (annotate stats of one sample test in histogram plot) is not yet implemented.')

        finish_show_and_save_plot(ax, params)

    else: # if plot_type not in list of supported options
        if type(plot_type) != str:
            raise TypeError('plot_type must be of type string and one of the following options:\n \
                            ["stripplot", "boxplot", "boxplot with stripplot overlay", "violinplot", "violinplot with stripplot overlay", "histogram"]')
        else:
            raise ValueError('plot_type must be one of the following options:\n \
                             ["stripplot", "boxplot", "boxplot with stripplot overlay", "violinplot", "violinplot with stripplot overlay", "histogram"]')




# Cell
def annotate_stats_one_sample(ax, df, params):
    l_stats_to_annotate = params['l_stats_to_annotate']

    if len(l_stats_to_annotate) > 0:
        max_total = df[params['data_col']].max()
        y_shift_annotation_line = max_total * params['distance_brackets_to_data']
        y_shift_annotation_text = y_shift_annotation_line*0.5*params['distance_stars_to_brackets']

        # Set initial y
        y = max_total + y_shift_annotation_line

        # Add check whether group level ANOVA / Kruska-Wallis-ANOVA is significant
        pval = params['results']['summary']['pairwise_comparisons'].iloc[0, :]['p-val']
        if pval <= 0.001:
            stars = '***'
        elif pval <= 0.01:
            stars = '**'
        elif pval <= 0.05:
            stars = '*'
        else:
            stars = 'n.s.'
        ax.text(0, y+y_shift_annotation_text, stars, ha='center', va='bottom', color='k',
                     fontsize=params['fontsize_stars'], fontweight=params['fontweight_stars'])
    return ax

# Cell
def plot_mma(df, plot_type = 'boxplot with stripplot overlay', params = DEFAULT_PARAMS):
    "Handles all the plotting that is currently available for datasets analyzed with a Mixed-Model ANOVA."
    if type(params) != dict:
        raise TypeError('params must be a dictionary')

    if 'data_col' not in list(params.keys()):
        params['data_col'] = df.columns[0]
        params['group_col'] = df.columns[1]
        params['session_col'] = df.columns[2]
        #params['l_x_order'] = list(df[params['session_col']].unique())
        #params['l_hue_order'] = list(df[params['group_col']].unique())

    for elem in l_required_keys_mma:
        if elem not in list(params.keys()):
            params[elem] = DEFAULT_PARAMS[elem]

    if plot_type in ['pointplot', 'boxplot', 'boxplot with stripplot overlay', 'violinplot', 'violinplot with stripplot overlay']:

        fig, ax = initialize_plot(params)

        if plot_type == 'pointplot':
            sns.pointplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          hue = params['group_col'], hue_order = params['l_hue_order'], palette = params['color_palette'],
                          dodge = True, ci = 'sd', err_style = 'bars', capsize = 0, ax = ax)
        elif plot_type == 'boxplot':
            sns.boxplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                        hue = params['group_col'], hue_order = params['l_hue_order'], palette = params['color_palette'], ax = ax)
        elif plot_type == 'boxplot with stripplot overlay':
            sns.boxplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                        hue = params['group_col'], hue_order = params['l_hue_order'], palette = params['color_palette'], ax = ax, showfliers = False)
            sns.stripplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          hue = params['group_col'], hue_order = params['l_hue_order'], dodge = True, color = 'k', size = params['set_marker_size'])
        elif plot_type == 'violinplot':
            sns.violinplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                           hue = params['group_col'], hue_order = params['l_hue_order'], palette = params['color_palette'],
                           width = 0.8, cut = 0, ax = ax)
        elif plot_type == 'violinplot with stripplot overlay':
            sns.violinplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                           hue = params['group_col'], hue_order = params['l_hue_order'], palette = params['color_palette'],
                           width = 0.8, cut = 0, ax = ax)
            sns.stripplot(data = df, x = params['session_col'], y = params['data_col'], order = params['l_xlabel_order'],
                          hue = params['group_col'], hue_order = params['l_hue_order'], dodge = True, color = 'k', size = params['set_marker_size'])

        if plot_type in ['boxplot', 'boxplot with stripplot overlay', 'violinplot', 'violinplot with stripplot overlay']:
            ax = annotate_stats_mma(ax, df, params)
        elif plot_type == 'pointplot':
            ax = annotate_stats_mma_pointplot(ax, df, params)

        if params['set_show_legend'] == True:
            if plot_type == 'pointplot':
                ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
            if plot_type in ['boxplot', 'boxplot with stripplot overlay', 'violinplot', 'violinplot with stripplot overlay']:
                handles, labels = ax.get_legend_handles_labels()
                new_handles = handles[:len(params['l_hue_order'])]
                new_labels = labels[:len(params['l_hue_order'])]
                ax.legend(new_handles, new_labels, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
        else:
            ax.get_legend().remove()

        finish_show_and_save_plot(ax, params)

    else: # if plot_type not in list of supported options
        if type(plot_type) != str:
            raise TypeError('plot_type must be of type string and one of the following options:\n \
                            ["stripplot", "boxplot", "boxplot with stripplot overlay", "violinplot", "violinplot with stripplot overlay"]')
        else:
            raise ValueError('plot_type must be one of the following options:\n \
                             ["stripplot", "boxplot", "boxplot with stripplot overlay", "violinplot", "violinplot with stripplot overlay"]')




# Cell
def annotate_stats_mma(ax, df, params):

    l_stats_to_annotate = params['l_stats_to_annotate']
    group_col = params['group_col']
    data_col = params['data_col']
    session_col = params['session_col']
    l_sessions = params['l_sessions']
    distance_brackets_to_data = params['distance_brackets_to_data']
    annotation_brackets_factor = params['annotation_brackets_factor']
    distance_stars_to_brackets = params['distance_stars_to_brackets']
    l_xlabel_order = params['l_xlabel_order']
    l_hue_order = params['l_hue_order']

    if len(l_stats_to_annotate) > 0:
        l_to_annotate_ordered = []
        for session_id in l_sessions:
            l_temp = [elem for elem in l_stats_to_annotate if elem[2]==session_id]
            for elem in l_temp:
                abs_mean_difference = abs(df.loc[(df[group_col]==elem[0]) & (df[session_col]==elem[2]), data_col].mean()-
                                          df.loc[(df[group_col]==elem[1]) & (df[session_col]==elem[2]), data_col].mean())
                l_temp[l_temp.index(elem)] = elem+(abs_mean_difference,)
            l_temp.sort(key=sort_by_third)
            l_to_annotate_ordered = l_to_annotate_ordered+l_temp

        df_temp = params['results']['summary']['pairwise_comparisons'].copy()

        max_total = df[data_col].max()
        y_shift_annotation_line = max_total * distance_brackets_to_data
        brackets_height = y_shift_annotation_line*0.5*annotation_brackets_factor
        y_shift_annotation_text = brackets_height + y_shift_annotation_line*0.5*distance_stars_to_brackets

        for elem in l_to_annotate_ordered:
            group1, group2, session_id, abs_mean_difference = elem

            if l_to_annotate_ordered.index(elem) == 0:
                n_previous_annotations_in_this_session_id = 0
            elif session_id == prev_session:
                n_previous_annotations_in_this_session_id = n_previous_annotations_in_this_session_id + 1
            else:
                n_previous_annotations_in_this_session_id = 0

            y = max_total + y_shift_annotation_line + y_shift_annotation_line*n_previous_annotations_in_this_session_id*3

            width = 0.8
            x_base = l_xlabel_order.index(session_id) - width/2 + width/(2*len(l_hue_order))
            x1 = x_base + width/len(l_hue_order)*l_hue_order.index(group1)
            x2 = x_base + width/len(l_hue_order)*l_hue_order.index(group2)

            stars = get_stars_str(df_temp.loc[df_temp[session_col] == session_id], group1, group2, params)

            ax.plot([x1, x1, x2, x2], [y, y+brackets_height, y+brackets_height, y], color='k', lw=params['linewidth_annotations'])
            ax.text((x1+x2)/2, y+y_shift_annotation_text, stars, ha='center', va='bottom',
                     fontsize=params['fontsize_stars'], fontweight=params['fontweight_stars'])

            prev_session = session_id

    return ax

# Cell
def annotate_stats_mma_pointplot(ax, df, params):

    l_stats_to_annotate = params['l_stats_to_annotate']
    group_col = params['group_col']
    data_col = params['data_col']
    session_col = params['session_col']
    l_sessions = params['l_sessions']
    distance_brackets_to_data = params['distance_brackets_to_data']
    annotation_brackets_factor = params['annotation_brackets_factor']
    distance_stars_to_brackets = params['distance_stars_to_brackets']
    l_xlabel_order = params['l_xlabel_order']

    if len(l_stats_to_annotate) > 0:
        l_to_annotate_ordered = []
        for session_id in l_sessions:
            l_temp = [elem for elem in l_stats_to_annotate if elem[2]==session_id]
            for elem in l_temp:
                abs_mean_difference = abs(df.loc[(df[group_col]==elem[0]) & (df[session_col]==elem[2]), data_col].mean()-
                                          df.loc[(df[group_col]==elem[1]) & (df[session_col]==elem[2]), data_col].mean())
                l_temp[l_temp.index(elem)] = elem+(abs_mean_difference,)
            l_temp.sort(key=sort_by_third)
            l_to_annotate_ordered = l_to_annotate_ordered+l_temp

        df_temp = params['results']['summary']['pairwise_comparisons'].copy()

        for elem in l_to_annotate_ordered:
            group1, group2, session_id, abs_mean_difference = elem

            if l_to_annotate_ordered.index(elem) == 0:
                n_previous_annotations_in_this_session_id = 0
            elif session_id == prev_session:
                n_previous_annotations_in_this_session_id = n_previous_annotations_in_this_session_id + 1
            else:
                n_previous_annotations_in_this_session_id = 0

            x_shift_annotation_line = distance_brackets_to_data + distance_brackets_to_data * n_previous_annotations_in_this_session_id * 1.5
            brackets_height = distance_brackets_to_data*0.5*annotation_brackets_factor
            x_shift_annotation_text = brackets_height + distance_brackets_to_data*0.5*distance_stars_to_brackets

            x = l_xlabel_order.index(session_id) + x_shift_annotation_line
            y1=df.loc[(df[group_col] == group1) & (df[session_col] == session_id), data_col].mean()
            y2=df.loc[(df[group_col] == group2) & (df[session_col] == session_id), data_col].mean()

            stars = get_stars_str(df_temp.loc[df_temp[session_col] == session_id], group1, group2, params)

            ax.plot([x, x+brackets_height, x+brackets_height, x], [y1, y1, y2, y2], color='k', lw=params['linewidth_annotations'])
            ax.text(x+x_shift_annotation_text, (y1+y2)/2, stars, rotation=-90, ha='center', va='center',
                     fontsize=params['fontsize_stars'], fontweight=params['fontweight_stars'])

            prev_session = session_id

    return ax

# Cell
def sort_by_third(e):
    return e[3]