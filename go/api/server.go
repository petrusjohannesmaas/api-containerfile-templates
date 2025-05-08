package main

import (
    "encoding/json"
    "net/http"
)

type Response struct {
    Response string `json:"response"`
}

func handler(w http.ResponseWriter, r *http.Request) {
    res := Response{Response: "🎉 Your Go API is running"}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(res)
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}