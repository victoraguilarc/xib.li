var gulp = require('gulp');
var browserify = require('gulp-browserify');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var refresh = require('gulp-livereload');
var lr = require('tiny-lr');
var server = lr();
var minifyCSS = require('gulp-minify-css');
var embedlr = require('gulp-embedlr');

var paths = {
  dirs: {
    build: '.build'
  },
  images: 'app/**/*.{JPG,jpg,png,gif}',
  json: 'app/**/*.json',
  sass: 'app/**/*.scss',
  less: 'app/**/*.less',
};

// gulp.task('scripts', function() {
//     gulp.src(['app/src/**/*.js'])
//         .pipe(browserify())
//         .pipe(concat('dest.js'))
//         .pipe(gulp.dest('dist/build'))
//         .pipe(refresh(server))
// })

gulp.task('styles', function() {
    gulp.src(['app/css/style.less'])

        .pipe(minifyCSS())
        .pipe(gulp.dest('dist/build'))
        .pipe(refresh(server))
})

gulp.task('lr-server', function() {
    server.listen(35729, function(err) {
        if(err) return console.log(err);
    });
})

gulp.task('default', function() {
    // gulp.run('lr-server', 'scripts', 'styles');
    gulp.run('lr-server', 'styles');

    gulp.watch('web/static/js/**', function(event) {
        gulp.run('scripts');
    })

    gulp.watch('web/static/scss/**', function(event) {
        gulp.run('styles');
    })
})

// 'use strict';
// const { watch, series } = require('gulp');
//
//
// var gulp = require('gulp'),
//     browserSync = require("browser-sync"),
//     reload = browserSync.reload,
//     del = require('del'),
//     cleanCSS = require('gulp-clean-css'),
//     sass = require('gulp-sass');
//
// var path = {
//     bower: {
//         jquery: [
//             './bower_components/jquery/dist/jquery.min.js',
//             './dev/js/vendor/jquery/jquery.min.js']
//     },
//     dist: { // compiled files
//         css: './web/static/assets/css/',
//     },
//     src: { // development files
//         scss: [
//             './web/static/assets/scss/transactions.scss',
//             './web/static/assets/scss/errors.scss',
//             './web/static/assets/scss/home.scss',
//         ]
//     },
//     watch: { // watching files
//         js: './web/static/assets/js/**/*.js',
//         css: './web/static/assets/scss/**/*.scss',
//         fonts: './web/static/assets/css/fonts/**/*.*',
//         img: './web/static/assets/img/**/*.*',
//         assets: './web/static/assets/assets/*.*'
//     },
//     clean: './build'
// };
//
// var forceReload = {stream: true};
// gulp.task('style:build', function () {
//     return gulp.src(path.src.scss)
//         .pipe(sass())
//         // .pipe(cleanCSS())
//         .pipe(gulp.dest(path.dist.css))
//         .pipe(reload(forceReload));
// });
//
//
// // gulp.task('js:build', function () {
// //     gulp.src(path.src.js)
// //         .pipe(gulp.dest(path.dist.js));
// //
// //     return gulp.src(path.src.js)
// //         .pipe(gulp.dest(path.dist.js))
// //         .pipe(reload(forceReload));
// // });
//
//
//
// gulp.task('build', [
//     'style:build',
//     // 'js:build',
// ]);
//
// gulp.task('watch', function(){
//     watch([path.watch.css], function(event, cb) {
//         gulp.start('style:build');
//     });
//
//     // watch([path.watch.js], function(event, cb) {
//     //     gulp.start('js:build');
//     // });
//
// });
//
// gulp.task('clean', function (cb) {
//     del(path.clean, cb);
// });
//
// gulp.task('default', ['build', 'watch']);
