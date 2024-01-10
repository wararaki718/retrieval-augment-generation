package com.wararaki.sampleragapplication.model

import org.springframework.data.annotation.Id
import org.springframework.data.elasticsearch.annotations.Document
import org.springframework.data.elasticsearch.annotations.Field
import org.springframework.data.elasticsearch.annotations.FieldType

@Document(indexName = "rag")
data class Passage (
    @Id val id: String,
    @Field(type = FieldType.Text, name = "content") val content: String,
){}
