# Robot pozíció szimuláció
## A egy node véletlen (x, y) pozíciókat küld, míg eyűgy másik kiszámolja a távolságot az origótól.

A package két node-ból áll. A /position_publisher random x és y koordinátákat hirdet a /position topic-ra amiket a /position_subscriber fogad és kiszámolja milyen messze vanak az origótól a koordináták, majd azokat kiirja a konzolra. Megvalósítás ROS 2 Humble alatt.
