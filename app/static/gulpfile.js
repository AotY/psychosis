var gulp = require('gulp');
var rename = require("gulp-rename");
var uglify = require('gulp-uglify');
var cleanCSS = require('gulp-clean-css');
var pump = require('pump');

// Minify JavaScript
gulp.task('js', function () {
    return gulp.src([
        './js/*.js',
        '!./js/*.min.js'
    ])
        .pipe(uglify())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./dist/js'))
});


gulp.task('compress', function (cb) {
    pump([
            gulp.src('js/csrf.js'),
            uglify(),
            gulp.dest('dist/js')
        ],
        cb
    );
});


// Minify CSS
gulp.task('css', function () {
    return gulp.src([
        './css/*.css',
        './css/**/*.css',
        '!./css/*.min.css',
        '!./css/**/*.min.css'
    ])
        .pipe(cleanCSS())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./dist/css'));
});

