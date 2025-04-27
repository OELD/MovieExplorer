const { createApp } = Vue;

createApp({
  data() {
    return {
      movies: [],
      newMovie: { title: "", director: "", year: null }
    };
  },
  mounted() { this.fetchMovies(); },
  methods: {
    async fetchMovies() {
      const res = await fetch('http://localhost:8000/movies');
      this.movies = await res.json();
    },
    async addMovie() {
      const res = await fetch('http://localhost:8000/movies', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(this.newMovie)
      });
      const movie = await res.json();
      this.movies.push(movie);
      this.newMovie = { title: "", director: "", year: null };
    }
  }
}).mount('#app');
