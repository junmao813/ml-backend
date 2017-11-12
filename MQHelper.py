#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika

service_address = '39.106.70.4'


def send_message(queue_name, msg_body):

    # 发送消息~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 连接到rabbitmq服务器
    connection = pika.BlockingConnection(pika.ConnectionParameters(service_address))
    channel = connection.channel()

    # 声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，rabbitmq将会自动清除这些消息
    channel.queue_declare(queue=queue_name)

    # 发送消息到上面声明的hello队列，其中exchange表示交换器，能精确指定消息应该发送到哪个队列，
    # routing_key设置为队列的名称，body就是发送的内容
    channel.basic_publish(exchange='', routing_key=queue_name, body=msg_body)

    print(" [x] Sent Msg: ", msg_body)

    # 关闭链接
    connection.close()


def receive_message(queue_name, callback):

    # 接收消息~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    connection1 = pika.BlockingConnection(pika.ConnectionParameters(service_address))

    channel1 = connection1.channel()
    channel1.queue_declare(queue=queue_name)

    channel1.basic_consume(callback, queue=queue_name, no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel1.start_consuming()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % ((body).decode('UTF-8'),))


if __name__ == '__main__':
    send_message("hello", "一个新的消息")
    # receive_message("hello", callback)
