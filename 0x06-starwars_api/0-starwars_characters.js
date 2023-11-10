#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
request(url + movieId, function (error, response, body) {
    if (error) {
        console.error(error);
    }
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
        request(character, function (error, response, body) {
        if (error) {
            console.error(error);
        }
        console.log(JSON.parse(body).name);
        });
    }
    });