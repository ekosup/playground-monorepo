/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.{html,py}",
        "../**/templates/**/*.{html,py}",
        'node_modules/preline/dist/*.js',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('preline/plugin')
    ],
}
