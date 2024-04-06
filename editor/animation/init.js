requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function cryptarithm_solver_visualization(tgt_node, data) {
            if (!data || !data.ext) {
                return
            }

            /**
             * attr
             */
            const attr = {
                border: {
                    'stroke-width': '0.5px',
                },
            }

            /**
             * values
             */
            const input = data.in[0]
            const words = input
            const answer = input[input.length-1]
            const dict = data.ext.answer
            const grid_seize_px_w = 200
            const os = 13
            const columns = (answer.length + 1) * 2 + 1
            const rows = words.length
            const unit = grid_seize_px_w / columns
            const scale = 15 / columns

            // paper
            const paper = Raphael(tgt_node, grid_seize_px_w + (os * 2), (unit * rows) + (os * 2))

            /**
             * draw column_addition
             */
            function draw_column_addition(start_x, start_y, words) {
                // words
                words.forEach((word, i)=> {
                    word.split('').forEach((w, j) => {
                        paper.text(
                            unit * (answer.length - word.length + j + 1.5) + start_x,
                            unit * (i + 0.5) + start_y,
                            w
                        ).attr({'font-size': (10 * scale) + 'px'})
                    })
                })
                // plus
                paper.text(
                    unit * 0.5 + start_x,
                    unit * (rows - 2 + 0.5) + start_y,
                    '+'
                ).attr({'font-size': (10 * scale) + 'px'})
                // border
                paper.path([
                    'M', start_x, unit * (rows - 1) + start_y,
                    'h', unit * (answer.length + 1)]
                ).attr(attr.border)
            }

            /**
             * number_translation
             */
            const number_translation = (words => words.map(word => word.split('').map(w => dict[w]).join('')))

            draw_column_addition(os, os, words)
            draw_column_addition(unit * (answer.length + 2) + os, os, number_translation(words))
        }
        var io = new extIO({
            animation: function ($expl, data) {
               cryptarithm_solver_visualization(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
